// Persist the selected value of the temperature selector filter.
// Code based on `themes.js` in this repository.

// get the tenperature & diet selector dropdown form
let temperatureSelector = document.getElementById('temperature-selector');
let dietSelector = document.getElementById('diet-selector');


/** populate storage with the value form the selector form */
function storeFilters() {
    localStorage.setItem("temperatureFilter", temperatureSelector.value);
    localStorage.setItem("dietFilter", dietSelector.value);
    
    applyFilters();
}

/** filter recipes based on the value in storage */
function applyFilters() {
    // get the filter value from storage
    let currentTemparatureFilter = localStorage.getItem("temperatureFilter");
    let currentDietFilter = localStorage.getItem("dietFilter");

    // set the filter selector value to the one retrieved from storage
    temperatureSelector.value = currentTemparatureFilter;
    dietSelector.value = currentDietFilter;
}

function resetTemperature() {
    console.log("reset temperature")
    localStorage.setItem("temperatureFilter", "any temperature");
    temperatureSelector.value = "any temperature";
}

function resetDiet() {
    console.log("reset diet")
    localStorage.setItem("dietFilter", "any diet");
    dietSelector.value = "any diet";
}

temperatureSelector.addEventListener("change", storeFilters);
dietSelector.addEventListener("change", storeFilters);
temperatureSelector.addEventListener("change", resetDiet);
dietSelector.addEventListener("change", resetTemperature);
document.addEventListener("DOMContentLoaded", applyFilters)