# Amelia Sinclaire 2023
import math

from data_loader import get_data
from tests import TestAOC
import time

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
        start = time.time()
        self.init_data(data)
        print(f'Took {time.time()-start}s to initialize data structure.')

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

    def yield_seed_range_seeds(self):
        for seed in self.seed_ranges:
            seed_value, seed_range = seed.split('_')
            for i in range(int(seed_range)):
                yield str(int(seed_value)+i)


def part_one(data):
    g = Garden(data, generate_seed_ranges=False)
    min_location = math.inf
    for seed in g.seeds:
        loc = int(g.seed_to_location(seed))
        if loc < min_location:
            min_location = loc
    return min_location


def part_two(data):
    g = Garden(data, generate_seed_ranges=True)
    min_location = math.inf
    for seed in g.yield_seed_range_seeds():
        loc = int(g.seed_to_location(seed))
        if loc < min_location:
            print(seed)
            min_location = loc
    return min_location


def main():
    data = get_data()
    tester = TestAOC(test1_answer=35, test2_answer=46)
    tester.test_all()

    if data is not None:
        print('Calculating answer(s)...')
        start = time.time()
        p1 = part_one(data)
        t = time.time() - start
        print(f'Part one: {p1} in {t} seconds.')  # 0.001 seconds
        # start = time.time()
        # # p2 = part_two(data)
        # t = time.time() - start
        # print(f'Part two: {p2} in {t} seconds.')


if __name__ == '__main__':
    main()
