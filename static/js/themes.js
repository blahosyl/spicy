const bodyStyles = document.body.style;
let themeSelector = document.getElementById('theme-selector');
themeSelector.addEventListener('change',changeTheme);

function changeTheme() {
    if (themeSelector.value == 'green') {
        bodyStyles.setProperty('--gray', 'green');
    }
    else {
        bodyStyles.setProperty('--gray', '#445261');
    }
}