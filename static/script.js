// ======= Mobile Menu =======
const mobileMenu = document.querySelector('.mobile-menu');
const navLinks = document.querySelector('.nav-links');
if (mobileMenu && navLinks) {
  mobileMenu.addEventListener('click', () => {
    navLinks.classList.toggle('active');
  });

  document.querySelectorAll('.nav-links a').forEach(link => {
    link.addEventListener('click', () => navLinks.classList.remove('active'));
  });
}

// ======= Contact Form =======
const form = document.getElementById('contactForm');
if (form) {
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    alert('Thank you! Your message has been sent.');
    form.reset();
  });
}

// ======= Gallery Filter =======
function filterGallery(category) {
  const items = document.querySelectorAll('.gallery-item');
  const buttons = document.querySelectorAll('.filter-btn');
  if (!items.length || !buttons.length) return;

  // Update active button
  buttons.forEach(btn => {
    btn.classList.remove('active');
    if (
      btn.textContent.toLowerCase().includes(category) ||
      (category === 'all' && btn.textContent.toLowerCase().includes('all'))
    ) {
      btn.classList.add('active');
    }
  });

  // Show/hide items
  items.forEach(item => {
    if (category === 'all' || item.getAttribute('data-category') === category) {
      item.style.display = 'block';
    } else {
      item.style.display = 'none';
    }
  });
}

// Initialize gallery on page load
window.addEventListener('load', () => {
  filterGallery('all');
});

// ======= Auto-hide Django Messages =======
setTimeout(() => {
  const messages = document.querySelector('.messages');
  if (messages) {
    messages.style.animation = 'fadeOut 0.6s forwards';
    setTimeout(() => messages.remove(), 600);
  }
}, 4000);
document.querySelectorAll('.nav-links a').forEach(a => { if (a.href === window.location.href) a.classList.add('active'); });
