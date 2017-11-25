// Program Name: manage_suites.py
// Organization: Student Projects and Research Committee at Auburn University
// Project: Lab Assistant
// Description: Collects all of the suites and parses through each to determine correct response.

// from suites.defaultsuite import *
//     from suites.labsuite import *
//     from suites.homesuite import *
//     from suites.weathersuite import *
//     from suites.fallbacksuite import *
// import socket

// suites = [LabSuite(), HomeSuite(), WeatherSuite(), DefaultSuite(), FallBackSuite()];
var suites = [DefaultSuite()];
var suite;

function getresponse(user_message){
    if (user_message.length > 0) {
        for (suite in suites){
            if (!suite.checkcommand(user_message)){
                return suite.response;
            }
        }
    }
}

function is_connected() {
    const server = "www.google.com"

    try {
        // see if we can resolve the host name -- tells us if there is a DNS listening
        var host = socket.gethostbyname(server);
        // connect to the host -- tells us if the host is actually reachable
        var socket.create_connection((host, 80), 2);
        return True;
    }
    catch(err){

    }
    return False;
}