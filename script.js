function calSI(){
    const principal = document.getElementById('principal').value;
    const rate = document.getElementById('rate').value;
    const time = document.getElementById('time').value;

    if (principal && rate && time) {
        const intrest =(principal*rate*time)/100;
        document.getElementById('result').innerText = 'The Simple Intrest is : ${intrest}';
    } else{
        document.getElementById('result').innerText='Please fill all fields.';
    }
}