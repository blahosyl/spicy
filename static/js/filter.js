// Persist the selected value of the temperature and diet filter.
// Code based on `themes.js` in this repository.

// get the temperature & diet selector dropdown forms
let temperatureSelector = document.getElementById('temperature-selector');
let dietSelector = document.getElementById('diet-selector');
let tasteSelector = document.getElementById('taste-selector');

/** populate storage with the value form the selector form */
function storeFilters() {

    localStorage.setItem("temperatureFilter", temperatureSelector.value);
    localStorage.setItem("dietFilter", dietSelector.value);
    localStorage.setItem("tasteFilter", tasteSelector.value);
    
    applyFilters();
}

/** filter recipes based on the value in storage */
function applyFilters() {

    // get the filter value from storage
    let currentTemparatureFilter = localStorage.getItem("temperatureFilter");
    let currentDietFilter = localStorage.getItem("dietFilter");
    let currentTasteFilter = localStorage.getItem("tasteFilter");

    // set the filter selector value to the one retrieved from storage
    temperatureSelector.value = currentTemparatureFilter;
    dietSelector.value = currentDietFilter;
    tasteSelector.value = currentTasteFilter;
}

/** reset the temperature filter form and storage value*/
function resetTemperature() {
    temperatureSelector.value = "any temperature";
    localStorage.setItem("temperatureFilter", "any temperature");
}

/** reset the diet filter form and storage value*/
function resetDiet() {
    dietSelector.value = "any diet";
    localStorage.setItem("dietFilter", "any diet");
}

/** reset the taste filter form and storage value*/
function resetTaste() {
    tasteSelector.value = "any taste";
    localStorage.setItem("tasteFilter", "any taste");
}

/** if the URL doesn't include the string 'filter', reset all filters */
function resetAllFilters() {
    if (!window.location.href.includes('filter')) {
        console.log("reset all filters")

        localStorage.setItem("temperatureFilter", "any temperature");
        temperatureSelector.value = "any temperature";

        localStorage.setItem("dietFilter", "any diet");
        dietSelector.value = "any diet";

        localStorage.setItem("tasteFilter", "any taste");
        tasteSelector.value = "any taste";
    }
}

temperatureSelector.addEventListener("change", storeFilters);
temperatureSelector.addEventListener("change", resetDiet);
temperatureSelector.addEventListener("change", resetTaste);

dietSelector.addEventListener("change", storeFilters);
dietSelector.addEventListener("change", resetTemperature);
dietSelector.addEventListener("change", resetTaste);

tasteSelector.addEventListener("change", storeFilters);
tasteSelector.addEventListener("change", resetTemperature);
tasteSelector.addEventListener("change", resetDiet);

document.addEventListener("DOMContentLoaded", applyFilters)
document.addEventListener("DOMContentLoaded", resetAllFilters);
