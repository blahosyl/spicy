// Persist the selected value of the temperature and diet filter.
// Code based on `themes.js` in this repository.

// get the temperature & diet selector dropdown forms
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
    temperatureSelector.value = "any temperature";
    localStorage.setItem("temperatureFilter", "any temperature");

}

/** reset the diet filter form and storage value*/
function resetDiet() {
    dietSelector.value = "any diet";
    localStorage.setItem("dietFilter", "any diet");
}

/** if the URL doesn't include the string 'filter', reset all filters */
function resetAllFilters() {
    if (!window.location.href.includes('filter')) {
        console.log("reset all filters")

        localStorage.setItem("temperatureFilter", "any temperature");
        temperatureSelector.value = "any temperature";

        localStorage.setItem("dietFilter", "any diet");
        dietSelector.value = "any diet";
    }
}

temperatureSelector.addEventListener("change", storeFilters);
dietSelector.addEventListener("change", storeFilters);
temperatureSelector.addEventListener("change", resetDiet);
dietSelector.addEventListener("change", resetTemperature);
document.addEventListener("DOMContentLoaded", applyFilters)

document.addEventListener("DOMContentLoaded", resetAllFilters);
