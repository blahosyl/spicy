// Governs the behaviour of the temperature, diet, taste and texture filters.
// Only one filter can be active at a time.
// Code based on `themes.js` in this repository.

// get the temperature & diet selector dropdown forms
let temperatureSelector = document.getElementById('temperature-selector');
let dietSelector = document.getElementById('diet-selector');
let tasteSelector = document.getElementById('taste-selector');
let textureSelector = document.getElementById('texture-selector');

/** populate storage with the value form the selector form */
function storeFilters() {

    localStorage.setItem("temperatureFilter", temperatureSelector.value);
    localStorage.setItem("dietFilter", dietSelector.value);
    localStorage.setItem("tasteFilter", tasteSelector.value);
    localStorage.setItem("textureFilter", textureSelector.value);
    
    applyFilters();
}

/** filter recipes based on the value in storage */
function applyFilters() {

    // get the filter value from storage
    let currentTemparatureFilter = localStorage.getItem("temperatureFilter");
    let currentDietFilter = localStorage.getItem("dietFilter");
    let currentTasteFilter = localStorage.getItem("tasteFilter");
    let currentTextureFilter = localStorage.getItem("textureFilter");

    // set the filter selector value to the one retrieved from storage
    temperatureSelector.value = currentTemparatureFilter;
    dietSelector.value = currentDietFilter;
    tasteSelector.value = currentTasteFilter;
    textureSelector.value = currentTextureFilter;
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

/** reset the texture filter form and storage value*/
function resetTexture() {
    textureSelector.value = "any texture";
    localStorage.setItem("textureFilter", "any texture");
}

/** if the URL doesn't include the string 'filter', reset all filters */
function resetAllFilters() {
    if (!window.location.href.includes('filter')) {

        resetTemperature();

        resetDiet();

        resetTaste();
        
        resetTexture();
    }
}

// if a filter is changed, store its value and reset all other filters

temperatureSelector.addEventListener("change", storeFilters);
temperatureSelector.addEventListener("change", resetDiet);
temperatureSelector.addEventListener("change", resetTaste);
temperatureSelector.addEventListener("change", resetTexture);

dietSelector.addEventListener("change", storeFilters);
dietSelector.addEventListener("change", resetTemperature);
dietSelector.addEventListener("change", resetTaste);
dietSelector.addEventListener("change", resetTexture);


tasteSelector.addEventListener("change", storeFilters);
tasteSelector.addEventListener("change", resetTemperature);
tasteSelector.addEventListener("change", resetDiet);
tasteSelector.addEventListener("change", resetTexture);

textureSelector.addEventListener("change", storeFilters);
textureSelector.addEventListener("change", resetTemperature);
textureSelector.addEventListener("change", resetDiet);
textureSelector.addEventListener("change", resetTaste);

// when loading the home page, reset the filters
document.addEventListener("DOMContentLoaded", resetAllFilters);
