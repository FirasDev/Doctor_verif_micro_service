const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const fileUpload = require('express-fileupload');
const fs = require('fs');
const { once } = require('events');

//initialization
app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({extended: true}));
app.use(bodyParser.json());
app.use(fileUpload());



app.post('/verif_doc', (req,res)=>{
    const file = req.files.file;
    const fileName = file.name;
    const filePath = './diploma/downloads/' + fileName;

    console.log(filePath);

    file.mv(filePath, async(err)=>{
        try{
       const verif_result = await verif(fileName);
         
        if (verif_result)
        {
            res.status(200).send("Verified");
        }
        else{
            console.log("===="+verif_result+"=====");
            res.status(200).send("Not verified");
        }
    }catch(err){
        console.log('Error : failed to download file');
                console.log(err);
                return res.status(500).send(err);
    }
    });
 
});


//calling python script here
const verif = async (fileName) => {

    var printedString = "";
    var isVerified = false;
    
    // Function to convert an Uint8Array to a string
    var uint8arrayToString = function(data){
        return String.fromCharCode.apply(null, data);
    };

    const spawn = require('child_process').spawn;

    //adding python executable & py file path
    const scriptExecution = spawn('python',['-u', './diploma/app.py']);

    // Write data 
    var data = JSON.stringify([fileName]);
    
    scriptExecution.stdin.write(data);
    // End data write
    scriptExecution.stdin.end();

    // Handle normal output
    scriptExecution.stdout.on('data', (data) => {
        printedString += uint8arrayToString(data);
    });

    // Handle error output
    scriptExecution.stderr.on('data', (data) => {
        // As said before, convert the Uint8Array to a readable string.
        console.log(uint8arrayToString(data));
    });

    scriptExecution.on('exit', (code) => {
        if (printedString.includes("verified")){
            console.log("printed"+printedString+"printed")
            isVerified = true;
        }
        console.log("Process quit with code : " + code);
    });
    await once(scriptExecution, 'close')
    console.log(isVerified);
    return isVerified;
}

function sleep(time, callback) {
    var stop = new Date().getTime();
    while(new Date().getTime() < stop + time) {
        ;
    }
    callback();
}

app.listen(3066, ()=>{
    console.log('Server is listening on port 3000');
});