fn main() {
    let text = include_str!("input.txt").lines().collect::<Vec<_>>();

    let mut values: Vec<Vec<char>> = vec![];

    for (x, line) in text.clone().into_iter().enumerate() {
        if line.chars().next().unwrap_or(' ') == '[' {
            values.push(vec![]);
            let mut index = 1;
            let chars: Vec<char> = line.chars().collect();
            for c in 0..chars.len() {
                if c == index {
                    values[x].push(chars[c]);
                    index += 4;
                }
            }
        }
    }

    let mut stacks: Vec<Vec<char>> = vec![];
    let mut stacks2: Vec<Vec<char>> = vec![];
    for _i in 0..values.len()+1 {
        stacks.push(vec![]);
        stacks2.push(vec![]);
    }
    for i in 0..stacks.len() {
        for line in values.clone().iter().rev() {
            if line[i] != ' ' {
                stacks[i].push(line[i]);
                stacks2[i].push(line[i]);
            }
        }
    }

    for (x, line) in text.clone().into_iter().enumerate() {
        if x >= values.len()+2 {
            let mut cmd: Vec<usize> = vec![];
            let words = line.split(' ');
            for i in words {
                let b = i.parse::<usize>().unwrap_or(0);
                if i.parse::<usize>().unwrap_or(0) != 0 {
                    cmd.push(b);
                }
            }
            let mut buf: Vec<char> = vec![];
            for _i in 0..cmd[0] {
                let temp = stacks[cmd[1]-1].pop().unwrap();
                let temp2 = stacks2[cmd[1]-1].pop().unwrap();
                buf.push(temp2);
                stacks[cmd[2]-1].push(temp);
            }
            for _m in 0..buf.len() {
                stacks2[cmd[2]-1].push(buf.pop().unwrap());
            }
        } 
    }

    println!("CrateMover 9000");
    for mut i in stacks {
        println!("{}", i.pop().unwrap())
    }
    println!("CrateMover 9001");
    for mut i in stacks2 {
        println!("{}", i.pop().unwrap())
    }
}


