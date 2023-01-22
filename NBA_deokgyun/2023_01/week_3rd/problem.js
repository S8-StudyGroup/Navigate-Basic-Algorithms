function solution(babbling) {
    let answer = 0;
    let speak3 = ['aya','woo']
    let speak2 = ['ye','ma']
    for (let i=0;i<babbling.length;i++) {
        let j = 0;
        let can_speak = 1;
        let prev_speak = '';
        while (j < babbling[i].length) {
            let speaking3 = babbling[i].slice(j,j+3)
            let speaking2 = babbling[i].slice(j,j+2)
            if (speak3.some((x) => speaking3 != prev_speak && speaking3 === x )) {
                j += 3;
                prev_speak = speaking3;
                continue;
            }
            
            else if (speak2.some((x) => speaking2 != prev_speak && speaking2 === x)) {
                j += 2;
                prev_speak = speaking2;
                // console.log("?")
                continue;
            }
            else {
                can_speak = 0;
                break;
            }
        }
        if (can_speak)
            answer++;
    }
    return answer;
}