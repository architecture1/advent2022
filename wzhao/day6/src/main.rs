const LENGTH: usize = 4;
fn main() {
    let text: Vec<char> = include_str!("input.txt").lines().collect::<Vec<_>>()[0].chars().collect();
    for i in 0..text.len() {
        let mut seen = std::collections::BTreeSet::new();
        for j in i..i+LENGTH {
            if !seen.insert(text[j]) {
                break;
            }
        }
        if seen.len() == LENGTH {
            println!("{}", i+LENGTH);
            break;
        }
    }
}
