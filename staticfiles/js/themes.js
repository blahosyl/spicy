const bodyStyles = document.body.style;
let themeSelector = document.getElementById('theme-selector');
themeSelector.addEventListener('change',changeTheme);

function changeTheme() {
    if (themeSelector.value == 'green') {
        bodyStyles.setProperty('--dark-highlight', '#1b871d');
        bodyStyles.setProperty('--highlight', '#7ef075');
        bodyStyles.setProperty('--light-highlight', '#ceedcc');

    }
    else {
        bodyStyles.setProperty('--dark-highlight', '#D7410F');
        bodyStyles.setProperty('--highlight', '#FD7E14');
        bodyStyles.setProperty('--light-highlight', '#f7ddcf');
    }
}