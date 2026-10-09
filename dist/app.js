const menuButton = document.querySelector('.menu-toggle');
const menu = document.querySelector('#menu');
function closeMenu() {
  menu.classList.remove('open');
  menuButton.setAttribute('aria-expanded', 'false');
}
menuButton.addEventListener('click', () => {
  const open = menuButton.getAttribute('aria-expanded') !== 'true';
  menuButton.setAttribute('aria-expanded', String(open));
  menu.classList.toggle('open', open);
});
menu.querySelectorAll('a').forEach(link => link.addEventListener('click', closeMenu));
document.addEventListener('keydown', event => { if (event.key === 'Escape') closeMenu(); });
const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
const desktop = window.matchMedia('(min-width: 1001px)');
const header = document.querySelector('.header');
const whatsapp = document.querySelector('.whatsapp-float');
const portrait = document.querySelector('.portrait');
let framePending = false;
function updateScroll() {
  const scroll = window.scrollY;
  header.classList.toggle('is-scrolled', scroll > 16);
  whatsapp?.classList.toggle('is-scrolled', scroll > 240);
  if (portrait) {
    const enabled = desktop.matches && !reducedMotion.matches;
    portrait.classList.toggle('has-parallax', enabled);
    portrait.style.setProperty('--parallax-offset', `${enabled ? Math.min(scroll * 0.045, 18) : 0}px`);
  }
  framePending = false;
}
window.addEventListener('scroll', () => {
  if (!framePending) {
    framePending = true;
    window.requestAnimationFrame(updateScroll);
  }
}, { passive: true });
window.addEventListener('pageshow', updateScroll);
desktop.addEventListener('change', updateScroll);
updateScroll();
let revealObserver;
const revealTargets = document.querySelectorAll('.section-heading, .service-card, .approach-statement, .approach-copy, .steps article, .questions > div, .detail-context > div, .situation-list, .prepare > div, .contact > h2');
if ('IntersectionObserver' in window && !reducedMotion.matches) {
  revealObserver = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.08, rootMargin: '0px 0px -24px 0px' });
  revealTargets.forEach(element => {
    // Keep content already in view visible, including anchor destinations.
    if (element.getBoundingClientRect().top < window.innerHeight) return;
    element.classList.add('scroll-reveal');
    if (element.matches('.service-card, .steps article')) {
      element.style.setProperty('--reveal-delay', `${([...element.parentElement.children].indexOf(element) % 3) * 70}ms`);
    }
    revealObserver.observe(element);
  });
}
reducedMotion.addEventListener('change', () => {
  updateScroll();
  if (reducedMotion.matches) {
    revealObserver?.disconnect();
    revealTargets.forEach(element => element.classList.add('is-visible'));
  }
});
document.querySelector('.footer-back-top')?.addEventListener('click', event => {
  event.preventDefault();
  header.focus({ preventScroll: true });
  window.scrollTo({ top: 0, behavior: reducedMotion.matches ? 'instant' : 'smooth' });
});
