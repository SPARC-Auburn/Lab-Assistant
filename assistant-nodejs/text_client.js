// Program Name: text_client.js
// Organization: Student Projects and Research Committee at Auburn University
// Project: Lab Assistant
// Description: A text based version of the virtual assistant.
// All commands are inputted and all responses are displayed in the terminal.

// import manage_suites
// from time import sleep
// from sys import stdout
const manage_suites = require("manage_suites")
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const assistant_name = "Karen";
const assistant_purpose = "to assist SPARC members";
const assistant_label = assistant_name.upper() + " > ";

console.log(assistant_label + "My name is " + assistant_name + " and I am here " + assistant_purpose +
    ". How may I help you?");
while manage_suites.is_connected(){
    rl.question("< ", function (user_message) {
        rl.close();
        if (user_message.length > 0) {
            console.log(assistant_label + manage_suites.getresponse(user_message))
        }
    });
}

// TODO: Add in print_slow function if desired.
// def print_slow(message):
// word_list = message.split()
// for word in word_list:
// stdout.write(word + " ")
// sleep(0.25)
// print("")
