fn main() {
    let input = include_str!("input.txt").lines().collect::<Vec<_>>();

    let mut path: Vec<(String, i32)> = vec![];
    let mut total = 0;
    let mut whole = 0;
    let mut min = 7000000;

    for i in input.clone() {
        let text: Vec<&str> = i.split(" ").collect();
        if text[0].parse::<i32>().is_ok() {
            whole += text[0].parse::<i32>().unwrap();
        }
    }

    let unused = 30000000 - (70000000 - whole);

    for (index, line) in input.iter().enumerate() {
        let text: Vec<&str> = line.split(" ").collect();
        match text[0] {
            "$" => match text[1] {
                "cd" => match text[2] {
                    "/" => path = vec![],
                    ".." => {
                        let popped = path.pop().unwrap();
                        if popped.1 <= 100000 {
                            total += popped.1;
                        }
                        if unused < popped.1 && popped.1 < min {
                            min = popped.1;
                        }
                    }
                    _ => {
                        path.push((text[2].to_string(), 0));
                    },
                }
                "ls" => (),
                _ => (),
            }
            "dir" => (),
            _ => {
                for mut i in &mut path {
                    i.1 += text[0].parse::<i32>().unwrap();
                }
            },
        }
        if index == input.len()-1 {
            if text[0].parse::<i32>().is_ok() {
                let num = text[0].parse::<i32>().unwrap();
                if num <= 100000 {
                    total += num;
                }
            }
        }
    }
    println!("{}", total);
    println!("{}", min);
}
