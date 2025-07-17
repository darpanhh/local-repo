// function savetoDb(data,success,failure){
//     let internetSpeed=Math.floor(Math.random()*10)+1;
//     if(internetSpeed>4){
//         success();
//     }
//     else{
//         failure();
//     }
// }

// savetoDb("apnacollege",()=>{
//     console.log("Success first data is saved");
//     savetoDb("darpangiri",()=>{
//         console.log("Success second data is saved");
//         savetoDb("web developer",()=>{
//             console.log("Success in third data");
//         },()=>{
//             console.log("failure in third data");
//         })
//     },()=>{
//         console.log("Failure in second data");
//     })
// },()=>{
//     console.log("failure in first data");
// })
// function savetoDb(data){
//     return new Promise((success,failure)=>{
//         let internetSpeed=Math.floor(Math.random()*10)+1;
//         if(internetSpeed>4){
//             success("success data was saved");
//         }
//         else{
//             failure("slow internet connection so not able to store");
//         }
//     }
// );
// }
// console.log(savetoDb("DarPangiri"));
// let request = savetoDb("DarPangiri")
// request
//     .then(()=>{
//     console.log("Promise resolved");
//     console.log(request);
//     }
//     )
//     .catch(()=>{
//     console.log("Promise rejected");
//     console.log(request);
//     }
//     );
// savetoDb("DarPangiri")
//     .then((result)=>{
//     console.log("data1 saved");
//     console.log("result of promise",result);
//     return savetoDb("apnacollege");
//     }
//     )
//     .then((result)=>{
//         console.log("Data 2 saved");
//         console.log("result of promise",result);
//         return savetoDb("helloworld");
//     })
//     .then((result)=>{
//         console.log("Data 3 saved");
//         console.log("result of promise",result);
//     })
//     .catch((error)=>{
//     console.log("Promise rejected");
//     console.log("error of promise",error);
//     }
//     );
// let jsonRes='{"fact":"Approximately earth is covered with earth around 60%","length":10}';
// let validRes=JSON.parse(jsonRes);
// console.log(validRes);
// async function greet(){
//     throw "404 page not found";
//     return "Hello world";
// }

// greet()
// .then((result)=>{
//     console.log("Promise was resolved");
//     console.log("result was:",result);

// })
// .catch((error)=>{
//     console.log("promise was rejected with error:",error);
// });
// let hello = async ()=>{
//     return 5;
// }
// async function getNum(){
//     return new Promise((resolve,reject)=>{
//         setTimeout(()=>{
//             let num = Math.floor(Math.random()*10)+1;
//             console.log(num);
//             resolve();
//         },1000);
//     });
// }
//  async function demo(){
//     await getNum();
//     await getNum();
//     await getNum();
//     getNum();
// }
// demo();
let h1 = document.querySelector("h1");
function changeColor(color,delay){
    return new Promise((resolve,reject)=>{
        setTimeout(()=>{
            let num = Math.floor(Math.random()*5)+1;
            if(num>3){
                reject("Promise rejected");
            }
            h1.style.color=color;
            resolve("color changed");
            console.log(`color changed to ${color}`);
        },delay);
    });
}
async function demo(){
    try{
        await changeColor("blue",1000);
        await changeColor("red",1000);
        await changeColor("orange",1000);
    }
    catch(err){
        console.log("Error caught");
        console.log(err);
    }
}
demo();