fn main() {
    let text = include_str!("input.txt").lines().collect::<Vec<_>>();

    let mut score = (0, 0);
    for line in text {
        let shape = line.split_once(" ").unwrap();
        let result = match shape {
            ("A", "X") => (4, 3),
            ("A", "Y") => (8, 4),
            ("A", "Z") => (3, 8),
            ("B", "X") => (1, 1),
            ("B", "Y") => (5, 5),
            ("B", "Z") => (9, 9),
            ("C", "X") => (7, 2),
            ("C", "Y") => (2, 6),
            ("C", "Z") => (6, 7),
            (_, _) => (0, 0),
        };
        score.0 += result.0;
        score.1 += result.1;
    }
    println!("{:?}", score);

}
