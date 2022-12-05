fn main() {
    let text = include_str!("input.txt").lines().collect::<Vec<_>>();

    let mut count = 0;
    let mut count2 = 0;
    for line in text {
        let nums  = line.split_once(",").unwrap();
        let num1 = nums.0.split_once("-").unwrap();
        let num2 = nums.1.split_once("-").unwrap();
        let x1 = num1.0.parse::<i32>().unwrap();
        let x2 = num1.1.parse::<i32>().unwrap();
        let y1 = num2.0.parse::<i32>().unwrap();
        let y2 = num2.1.parse::<i32>().unwrap();
        println!("{},{},{},{}", x1, x2, y1, y2);
        
        if x2-x1 >= y2-y1 {
            if x1 <= y1 && x2 >= y2 {
                count += 1;
            }
        }
        else if x2-x1 <= y2-y1 {
            if y1 <= x1 && y2 >= x2 {
                count += 1;
            }
        }

        if x1 <= y2 && y1 <= x2 {
            count2 += 1;
        }
    }
    println!("{}", count);
    println!("{}", count2);
}
