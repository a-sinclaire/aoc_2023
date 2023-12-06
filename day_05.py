# Amelia Sinclaire 2023
import math

from data_loader import get_data
from tests import TestAOC
from timing import time_it_decorator

import re


class Map:
    def __init__(self, data):
        self.map_dict = {}
        self.create_dict(data)

    def create_dict(self, data):
        for row in data:
            destination_range_start, source_range_start, range_length = row.split()
            # print(destination_range_start, source_range_start, range_length)
            # print(str(int(source_range_start)+int(i)), str(int(destination_range_start) + int(i)))
            self.map_dict[source_range_start+'_'+str(int(source_range_start)+int(range_length))] = destination_range_start

    def convert(self, source):
        for k, v in self.map_dict.items():
            source_range_start, source_range_end = k.split('_')
            if int(source_range_start) <= int(source) <= int(source_range_end):
                destination_range_start = v
                destination = int(source) - int(source_range_start) + int(destination_range_start)
                return str(destination)
        return source

    def un_convert(self, destinations):
        for k, v in self.map_dict.items():
            source_range_start, source_range_end = k.split('_')
            destination_range_start = int(v)
            range_length = int(source_range_end)-int(source_range_start)
            # print(f'destination range start: {v} | source range start: {source_range_start} | range length: {range_length}')
            # print(f'generating source range from {source_range_start}-{int(source_range_start)+range_length} if destination in range')
            # print(f'given destinations: {destinations}')
            # my_destinations = []
            # for i in range(range_length):
            #     destination = str(int(destination_range_start)+i)
            #     # print(f'checking destination {destination} is in given destinations: {destination in destinations}')
            #     if destination in destinations:
            #         my_destinations.append(destination)
            #         continue
            #     my_destinations.append()
            # if len(my_destinations) > 0:
            for destination in destinations:
                # print(destination)
                # find source that leads to d
                # print(f'is {destination} within destination range {destination_range_start}-{destination_range_start+range_length} : {destination_range_start <= int(destination) <= destination_range_start+range_length}')
                if destination_range_start <= int(destination) <= destination_range_start+range_length:
                    source = int(source_range_start)+(int(destination)-destination_range_start)
                    # print(f'{source} -> {destination}')
                    yield str(source)
                elif destination not in self.get_destinations():
                    yield str(destination)

    def get_destinations(self):
        for k, v in self.map_dict.items():
            source_range_start, source_range_end = k.split('_')
            destination_range_start = int(v)
            range_length = int(source_range_end)-int(source_range_start)
            # print(f'destination range start: {destination_range_start} | source range start: {source_range_start} | range length: {range_length}')
            # print(f'generating from {destination_range_start}-{destination_range_start+range_length}')
            for i in range(range_length):
                yield str(destination_range_start+i)

# d = ['50 98 2',
# '52 50 48']
# m = Map(d)
# print(m.map_dict)
# print(m.convert('79'))


class Garden:
    def __init__(self, data, generate_seed_ranges=False):
        self.seeds = []
        self.generate_seed_ranges = generate_seed_ranges
        self.seed_ranges = []
        self.seed_to_soil_map = None
        self.soil_to_fertilizer_map = None
        self.fertilizer_to_water_map = None
        self.water_to_light_map = None
        self.light_to_temperature_map = None
        self.temperature_to_humidity_map = None
        self.humidity_to_location_map = None
        self.init_data(data)

    def init_data(self, data):
        doing = {'doing_seeds': False,
                 'doing_seed_to_soil_map': False,
                 'doing_soil_to_fertilizer_map': False,
                 'doing_fertilizer_to_water_map': False,
                 'doing_water_to_light_map': False,
                 'doing_light_to_temperature_map': False,
                 'doing_temperature_to_humidity_map': False,
                 'doing_humidity_to_location_map': False}
        current_map = []
        for row in data:
            if row == '' or row == '\n':
                continue

            if re.search('seeds:', row):
                self.update_map(doing, current_map)
                doing = {x: False for x in doing}
                doing['doing_seeds'] = True
                self.seeds = [x.strip() for x in row.split(':')[1].split()]
                if self.generate_seed_ranges:
                    is_seed_value = True
                    seed_value = -1
                    for seed in self.seeds:
                        if is_seed_value:
                            seed_value = seed
                            is_seed_value = False
                        else:
                            seed_range = seed
                            self.seed_ranges.append(seed_value+'_'+seed_range)
                            is_seed_value = True
                current_map = []
                continue
            if re.search('seed-to-soil map:', row):
                self.update_map(doing, current_map)
                doing = {x: False for x in doing}
                doing['doing_seed_to_soil_map'] = True
                current_map = []
                continue
            if re.search('soil-to-fertilizer map:', row):
                self.update_map(doing, current_map)
                doing = {x: False for x in doing}
                doing['doing_soil_to_fertilizer_map'] = True
                current_map = []
                continue
            if re.search('fertilizer-to-water map', row):
                self.update_map(doing, current_map)
                doing = {x: False for x in doing}
                doing['doing_fertilizer_to_water_map'] = True
                current_map = []
                continue
            if re.search('water-to-light map:', row):
                self.update_map(doing, current_map)
                doing = {x: False for x in doing}
                doing['doing_water_to_light_map'] = True
                current_map = []
                continue
            if re.search('light-to-temperature map:', row):
                self.update_map(doing, current_map)
                doing = {x: False for x in doing}
                doing['doing_light_to_temperature_map'] = True
                current_map = []
                continue
            if re.search('temperature-to-humidity map:', row):
                self.update_map(doing, current_map)
                doing = {x: False for x in doing}
                doing['doing_temperature_to_humidity_map'] = True
                current_map = []
                continue
            if re.search('humidity-to-location map:', row):
                self.update_map(doing, current_map)
                doing = {x: False for x in doing}
                doing['doing_humidity_to_location_map'] = True
                current_map = []
                continue

            if not doing['doing_seeds']:
                current_map.append(row.strip())
                continue
        self.update_map(doing, current_map)

    def update_map(self, doing, map_list):
        if doing['doing_seed_to_soil_map']:
            self.seed_to_soil_map = Map(map_list)
            return
        if doing['doing_soil_to_fertilizer_map']:
            self.soil_to_fertilizer_map = Map(map_list)
            return
        if doing['doing_fertilizer_to_water_map']:
            self.fertilizer_to_water_map = Map(map_list)
            return
        if doing['doing_water_to_light_map']:
            self.water_to_light_map = Map(map_list)
            return
        if doing['doing_light_to_temperature_map']:
            self.light_to_temperature_map = Map(map_list)
            return
        if doing['doing_temperature_to_humidity_map']:
            self.temperature_to_humidity_map = Map(map_list)
            return
        if doing['doing_humidity_to_location_map']:
            self.humidity_to_location_map = Map(map_list)
            return

    def seed_to_location(self, seed):
        soil = self.seed_to_soil_map.convert(seed)
        fertilizer = self.soil_to_fertilizer_map.convert(soil)
        water = self.fertilizer_to_water_map.convert(fertilizer)
        light = self.water_to_light_map.convert(water)
        temperature = self.light_to_temperature_map.convert(light)
        humidity = self.temperature_to_humidity_map.convert(temperature)
        return self.humidity_to_location_map.convert(humidity)

    def locations_to_seeds(self, locations):
        # print(f'finding humidity values that maped to locations {locations}:')
        humidities = list(set(self.humidity_to_location_map.un_convert(locations)))
        # print(humidities)
        # print(f'finding temperature values that maped to humidities {humidities}:')
        temperatures = list(set(self.temperature_to_humidity_map.un_convert(humidities)))
        # print(temperatures)
        # print(f'finding lights values that maped to temperatures {humidities}:')
        lights = list(set(self.light_to_temperature_map.un_convert(temperatures)))
        # print(lights)
        # print(f'finding waters values that maped to lights {humidities}:')
        waters = list(set(self.water_to_light_map.un_convert(lights)))
        # print(waters)
        # print(f'finding fertilizers values that maped to waters {humidities}:')
        fertilizers = list(set(self.fertilizer_to_water_map.un_convert(waters)))
        # print(fertilizers)
        # print(f'finding soils values that maped to fertilizers {humidities}:')
        soils = list(set(self.soil_to_fertilizer_map.un_convert(fertilizers)))
        # print(soils)
        # print(f'finding seeds values that maped to soils {humidities}:')
        seeds = list(set(self.seed_to_soil_map.un_convert(soils)))
        # print(seeds)
        return seeds

    def yield_seed_range_seeds(self):
        for seed in self.seed_ranges:
            seed_value, seed_range = seed.split('_')
            for i in range(int(seed_range)):
                yield str(int(seed_value)+i)


@time_it_decorator
def part_one(data):
    g = Garden(data, generate_seed_ranges=False)
    min_location = math.inf
    for seed in g.seeds:
        loc = int(g.seed_to_location(seed))
        if loc < min_location:
            min_location = loc
    return min_location


@time_it_decorator
def part_two(data):
    g = Garden(data, generate_seed_ranges=True)
    min_location = math.inf
    for seed in g.yield_seed_range_seeds():
        loc = int(g.seed_to_location(seed))
        if loc < min_location:
            min_location = loc
    return min_location

# def part_two(data):
#     g = Garden(data, generate_seed_ranges=False)
#     locations = sorted(list(g.humidity_to_location_map.get_destinations()))
#     print(locations)
#     print(list(g.locations_to_seeds(['57'])))
#     # for loc in locations:
#     #     seeds = g.locations_to_seeds([loc])
#     #     for s in seeds:
#     #         print(s, '->', loc)
#             # if s in g.seeds:
#             #     return loc
#     #
#     # min_location = math.inf
#     # for seed in g.yield_seed_range_seeds():
#     #     loc = int(g.seed_to_location(seed))
#     #     if loc < min_location:
#     #         print(seed)
#     #         min_location = loc
#     return min(locations)


def main():
    data = get_data()
    tester = TestAOC(test1_answer=35, test2_answer=46)
    tester.test_all()

    if data is not None:
        print('Calculating answer(s)...')
        print(f'Part one: {part_one(data)}')
        # print(f'Part two: {part_two(data)}')  # estimation with current method = 51 hours


if __name__ == '__main__':
    main()
