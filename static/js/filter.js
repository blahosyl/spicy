// Persist the selected value of the temperature selector filter.
// Code based on `themes.js` in this repository.

// get the tenperature selector dropdown form
let temperatureSelector = document.getElementById('temperature-selector');

/** populate storage with the value form the color theme selector form */
function storeTemperatureFilter() {
    localStorage.setItem("temperatureFilter", temperatureSelector.value);
    
    applyTemperatureFilter();
}

/** set the site's color theme based on the value in storage */
function applyTemperatureFilter() {
    // get the theme value from storage
    let currentTemparatureFilter = localStorage.getItem("temperatureFilter");

    // set the theme selector value to the one retrieved from storage
    temperatureSelector.value = currentTemparatureFilter;
}

temperatureSelector.addEventListener("change", storeTemperatureFilter);
document.addEventListener("DOMContentLoaded", applyTemperatureFilter)