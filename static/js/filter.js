// Persist the selected value of the temperature selector filter.
// Code based on `themes.js` in this repository.

// get the tenperature selector dropdown form
let temperatureSelector = document.getElementById('temperature-selector');

// let searchButton = document.getElementsByClassName('btn-search')

window.addEventListener("DOMContentLoaded", (event) => {

    let button = document.getElementById('search-button"')
    if (button) {
        button.addEventListener("mousedown", resetTemperatureFilter);
        document.addEventListener("DOMContentLoaded", searchButtonColor);
    } else {
        console.log("no button!")
    }
});

/** check if storage is already populated */
function checkStorage() {
    if(!localStorage.getItem('temperature-selector')) {
        storeTemperatureFilter();
    } else {
        applyTemperatureFilter();
    }
}

/** populate storage with the value form the temperature selector form */
function storeTemperatureFilter() {
    localStorage.setItem("temperatureFilter", temperatureSelector.value);
    
    applyTemperatureFilter();
}

/** reset the value of the temperature filter in storage */
function resetTemperatureFilter() {
    localStorage.setItem("temperatureFilter", "");
    
    applyTemperatureFilter();
}

/** set the site's filtering based on the value in storage */
function applyTemperatureFilter() {
    if(!localStorage.getItem('temperature-selector')) {

        // get the temperature value from storage
        let currentTemparatureFilter = localStorage.getItem("temperatureFilter");

        // set the temperature selector value to the one retrieved from storage
        temperatureSelector.value = currentTemparatureFilter;
    } else {
        temperatureSelector.value = "";
    }
}

/** remove the  temperature filter value from storage */
function removeTemperatureFilter() {
    localStorage.removeItem('temperature-selector');
    alert('temperature value removed');
    console.log('temperature value removed');
    
    applyTemperatureFilter();
}

function searchButtonColor() {
    button.setAttribute("style", "border-color:purple;");
    console.log("button border color")
}

temperatureSelector.addEventListener("change", checkStorage);
document.addEventListener("DOMContentLoaded", applyTemperatureFilter);

