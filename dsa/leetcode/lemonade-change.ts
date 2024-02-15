function lemonadeChange(bills: number[]): boolean {
    let notes = {5:0, 10:0}
    for(let bill of bills){
        if(bill == 5){
            notes[5] += 1
        }else if(bill == 10){
            if(notes[5] == 0){
                return false
            }else{
                notes[5] -= 1
                notes[10] += 1
            }
        }else{
            if(notes[5] <= 2 && notes[10] == 0 || notes[5] == 0){
                return false
            }else if(notes[5] > 2 && notes[10] == 0){
                notes[5] -= 3
            }else{
                notes[10] -= 1
                notes[5] -=1

            }
        }
    }
    return true
};