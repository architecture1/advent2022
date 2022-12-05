use std::collections::HashMap;

fn main() {
    let alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    let alpha_chars: Vec<char> = alphabet.chars().collect();
    let mut alpha_number = HashMap::new();
    for number in 0..52 {
        alpha_number.insert(alpha_chars[number], number+1);
    }

    let text = include_str!("input.txt").lines().collect::<Vec<_>>();

    let mut count = 0;
    for line in text.clone() {
        let mut chars: Vec<char> = line.chars().collect();
        let length = chars.len();
        chars.insert(length / 2, '=');
        let new_string: String = chars.into_iter().collect();

        let sp = new_string.split_once('=').unwrap();

        let part1: Vec<char> = sp.0.chars().collect();
        let part2: Vec<char> = sp.1.chars().collect();

        let mut toggle = false;
        for c in part1 {
            if part2.contains(&c) && toggle == false {
                toggle = true;
                match alpha_number.get(&c) {
                    Some(n) => count += n,
                    None => println!("None"),
                }
            }
        }
    }

    println!("{}", count);

    let mut count2 = 0;
    let mut counter = 0;
    for index in 0..text.len()-2 {
        if counter == 0 {
            let mut toggle = false;
            counter = 2;
            let x: Vec<char> = text[index].chars().collect();
            for d in x {
                let y: Vec<char> = text[index+1].chars().collect();
                if y.contains(&d) && toggle == false {
                    let z: Vec<char> = text[index+2].chars().collect();
                    if z.contains(&d) {
                        toggle = true;
                        match alpha_number.get(&d) {
                            Some(n) => count2 += n,
                            None => println!("None"),
                        }
                    }
                }
            }
            // counter -= 1;
        }
        else {
            counter -= 1;
        }
    }

    println!("{}", count2);
}