use std::{
    cmp::{max, min},
    ops::Range,
};

use regex::Regex;

fn grab_all_integers(text: &str) -> Vec<usize> {
    let iter = Regex::new(r"\d+").unwrap();
    let iter = iter.find_iter(text);
    iter.map(|x| x.as_str().parse::<usize>().unwrap()).collect()
}

type SeedRange = Range<i64>;

#[derive(Debug, Clone, Copy)]
struct TransformationRange {
    destination_start: i64,
    origin_start: i64,
    length: i64,
}

impl TransformationRange {
    fn intersection_with_seed(&self, seed: &SeedRange) -> SeedRange {
        let &TransformationRange {
            origin_start,
            length,
            ..
        } = self;

        max(seed.start, origin_start)..min(seed.end, origin_start + length)
    }
}

fn main() {
    let input = include_str!("../input.txt").trim();

    let lines = input.lines().map(str::trim).collect::<Vec<&str>>();
    let (first_line, lines) = lines.split_first().unwrap();

    // Split sections on empty lines
    let sections = lines.split(|line| line.is_empty());

    let seed_input: Vec<i64> = grab_all_integers(first_line)
        .into_iter()
        .map(|x| x as i64)
        .collect::<Vec<i64>>();

    let mut seed_ranges = seed_input
        .chunks(2)
        .map(|range| range[0]..range[0] + range[1])
        .collect::<Vec<SeedRange>>();

    println!("Start seed count: {}", seed_ranges.len());

    for section in sections.into_iter() {
        let transformations = section
            .iter()
            .map(|x| {
                grab_all_integers(x)
                    .into_iter()
                    .map(|x| x as i64)
                    .collect::<Vec<i64>>()
            })
            .filter(|arr| !arr.is_empty())
            .map(|arr| TransformationRange {
                destination_start: arr[0],
                origin_start: arr[1],
                length: arr[2],
            })
            .collect::<Vec<TransformationRange>>();

        seed_ranges = seed_ranges
            .into_iter()
            .flat_map(|seed_range| transform_seed_range(seed_range, &transformations))
            .collect();

        println!("Updated seed range count: {}", seed_ranges.len());
    }

    dbg!(seed_ranges.iter().map(|range| range.start).min().unwrap());
}

fn transform_seed_range(
    seed_range: SeedRange,
    transformations: &[TransformationRange],
) -> Vec<SeedRange> {
    let mut unprocessed_seed_queue = vec![seed_range];
    let mut processed_seeds = vec![];

    while let Some(seed) = unprocessed_seed_queue.pop() {
        // Find transformation with intersection with the seed
        let transformation_to_apply = transformations.iter().find(|&transformation| {
            let intersection = transformation.intersection_with_seed(&seed);
            !intersection.is_empty()
        });

        let Some(&transformation) = transformation_to_apply else {
            // If there is no transformation to be done, consider the seed processed
            processed_seeds.push(seed);
            // Skip to the next seed in the queue
            continue;
        };

        let TransformationRange {
            destination_start,
            origin_start,
            length,
        } = transformation;

        let SeedRange {
            start: seed_start,
            end: seed_end,
        } = seed;

        let origin_end = origin_start + length;

        // Possible cases:
        //
        // 1. Seed is contained in transformation.
        // 2. Transformation doesn't include seed but includes seed's left boundary.
        // 3. Transformation doesn't include seed but includes seed's right boundary.
        // 4. Transformation is smaller than seed and fully contained in it.
        // 5. Transformation doesn't intersect with seed.
        //
        // Note: `It's possible that `4` is also `2` or `3`
        //
        // We need to make sure the following code covers all cases

        let offset = destination_start - origin_start;
        let intersection = transformation.intersection_with_seed(&seed);

        processed_seeds.push(Range {
            start: intersection.start + offset,
            end: intersection.end + offset,
        });

        if seed_start < origin_start {
            unprocessed_seed_queue.push(Range {
                start: seed_start,
                end: intersection.start - 1,
            });
        }

        if seed_end > origin_end {
            unprocessed_seed_queue.push(Range {
                start: intersection.end + 1,
                end: seed_end,
            });
        }
    }

    processed_seeds.into_iter().collect()
}