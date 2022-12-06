const LENGTH: usize = 14;

fn main() {
    let text = include_str!("input.txt").lines().collect::<Vec<_>>();

    for i in text {
        let chars: Vec<char> = i.chars().collect();
        for x in LENGTH..chars.len() {
            let mut count = 0;
            let mut seen: Vec<char> = vec![];
            for y in x-LENGTH..x {
                if !seen.contains(&chars[y]) {
                    count += 1;
                    seen.push(chars[y]);
                }
                else {
                    break;
                }
                if count >= LENGTH {
                    println!("{}", x);
                    break;
                }
            }
            if count >= LENGTH {
                break;
            }
        }
    }
}
