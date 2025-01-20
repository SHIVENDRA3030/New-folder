// JavaScript for 'DarkStar'

// Navbar search functionality
const searchInput = document.querySelector('.fnav .left input');
searchInput.addEventListener('input', (e) => {
    console.log(`Search query: ${e.target.value}`);
});

// Sign In button click
const signInButton = document.querySelector('.fnav .right button');
signInButton.addEventListener('click', () => {
    alert('Sign In functionality will be implemented soon!');
});

// Secondary nav links
const secondaryLinks = document.querySelectorAll('.sec-nav p');
secondaryLinks.forEach(link => {
    link.addEventListener('click', () => {
        console.log(`${link.textContent} clicked`);
    });
});

// Banner image click
const banner = document.querySelector('.banner img');
banner.addEventListener('click', () => {
    alert('Banner clicked!');
});

// Card images click
const cardImages = document.querySelectorAll('.card img');
cardImages.forEach((img, index) => {
    img.addEventListener('click', () => {
        alert(`Image ${index + 1} clicked!`);
    });
});


// Footer copyright alert
const copyright = document.querySelector('.footer .copyright');
copyright.addEventListener('click', () => {
    alert('DarkStar © 2024');
});
