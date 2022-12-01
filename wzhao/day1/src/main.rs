fn main() {
    let text = include_str!("input.txt").lines().collect::<Vec<_>>();

    let mut highest = 0; 
    let mut higher = 0;
    let mut high = 0;
    let mut count = 0;
    for line in text {
        if line == "" {
            if count > highest {
                high = higher;
                higher = highest;
                highest = count;
            }
            else if count > higher {
                high = higher;
                higher = count;
            }
            else if count > high {
                high = count;
            }
            count = 0;
        }
        else {
            count += line.parse::<i32>().unwrap();
        }
    }
    println!("Top Elf Calories: {}", highest);
    println!("Top 3 Elf Calories: {}", high+higher+highest);
}
