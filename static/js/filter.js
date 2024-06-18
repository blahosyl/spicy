// Persist the selected value of the temperature selector filter.
// Code based on `themes.js` in this repository.

// get the tenperature selector dropdown form
let temperatureSelector = document.getElementById('temperature-selector');

// let searchButton = document.getElementsByClassName('btn-search')



/** check if storage is already populated */
function checkStorage() {
    if(!localStorage.getItem('temperatureFilter')) {
        storeTemperatureFilter();
    } else {
        applyTemperatureFilter();
    }
}

function checkURL() {
    if (!window.location.href.includes('temp')) {
        resetTemperatureFilter();
    } else {
        console.log("INCLUDES 'temp'")
    }
}

/** populate storage with the value form the temperature selector form */
function storeTemperatureFilter() {
    localStorage.setItem("temperatureFilter", temperatureSelector.value);
    
    applyTemperatureFilter();
}

/** reset the value of the temperature filter in storage */
function resetTemperatureFilter() {
        localStorage.setItem("temperatureFilter", "pineapple");
        console.log("DOESN'T INCLUDE 'temp'")
    }
    applyTemperatureFilter();

/** set the site's filtering based on the value in storage */
function applyTemperatureFilter() {

        // get the temperature value from storage
        let currentTemparatureFilter = localStorage.getItem("temperatureFilter");

        // set the temperature selector value to the one retrieved from storage
        temperatureSelector.value = currentTemparatureFilter;
}

// /** remove the  temperature filter value from storage */
// function removeTemperatureFilter() {
//     if (!window.location.href.includes('temp')) {
//         localStorage.removeItem('temperature-selector');
//         console.log('temperature value removed');
//     }
    
//     // applyTemperatureFilter();
// }


window.addEventListener("DOMContentLoaded", (event) => {
});

// document.addEventListener("DOMContentLoaded", checkURL);
temperatureSelector.addEventListener("change", checkStorage);
document.addEventListener("DOMContentLoaded", applyTemperatureFilter);



