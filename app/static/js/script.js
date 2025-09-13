// Migrated from original root script.js
document.addEventListener('DOMContentLoaded', function(){
	const menuToggle = document.getElementById('menu-toggle');
	const navLinks = document.querySelector('.nav-links');
	if(menuToggle && navLinks){
		menuToggle.addEventListener('click', () => navLinks.classList.toggle('active'));
	}
	const fadeElements = document.querySelectorAll('.fade-in');
	const observer = new IntersectionObserver(entries => {
		entries.forEach(entry => { if(entry.isIntersecting){ entry.target.classList.add('visible'); } });
	});
	fadeElements.forEach(el => observer.observe(el));
});