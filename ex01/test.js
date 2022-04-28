list1 = [1,2,3]
console.log(list1)

// spread 지원 , list1이 들고 있는 요소들을 흩뿌린다.
list1 = [...list1, 4]

console.log(list1)

let user =[
    {id:1,
        username:"cos"}
]

user = {...user, id:2}

console.log(user)