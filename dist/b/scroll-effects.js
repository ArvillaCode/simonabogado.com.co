const menuButton = document.querySelector('.menu-toggle');
const menu = document.querySelector('#menu');
const header = document.querySelector('.header');
const whatsapp = document.querySelector('.whatsapp-float');
const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
const desktop = window.matchMedia('(min-width: 1001px)');
const photo = document.querySelector('.portrait, .detail-image');
let motionChoice = null;
try { motionChoice = localStorage.getItem('simon-motion'); } catch (_) {}
function motionEnabled() {
  return motionChoice === 'on' || (motionChoice !== 'off' && !reducedMotion.matches);
}
function applyMotionChoice() {
  document.documentElement.dataset.motion = motionEnabled() ? 'on' : 'off';
}
applyMotionChoice();

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

let framePending = false;
function updateScroll() {
  header.classList.toggle('is-scrolled', window.scrollY > 16);
  whatsapp?.classList.toggle('is-scrolled', window.scrollY > 240);
  if (photo) {
    const enabled = desktop.matches && motionEnabled();
    photo.classList.toggle('has-parallax', enabled);
    const offset = enabled ? Math.max(-24, Math.min(24, -photo.getBoundingClientRect().top * .065)) : 0;
    photo.style.setProperty('--photo-offset', `${offset}px`);
  }
  framePending = false;
}
function queueScroll() {
  if (framePending) return;
  framePending = true;
  window.requestAnimationFrame(updateScroll);
}
window.addEventListener('scroll', queueScroll, { passive: true });
window.addEventListener('resize', queueScroll, { passive: true });
window.addEventListener('pageshow', queueScroll);
desktop.addEventListener('change', queueScroll);
updateScroll();

// A separate choreography for each section, revealed once on entry.
const targets = new Set();
let observer;
function initializeEffects() {
  if (!('IntersectionObserver' in window) || !motionEnabled() || targets.size) return;
  observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('is-in');
      observer.unobserve(entry.target);
    });
  }, { threshold: .01, rootMargin: '0px 0px -20px 0px' });

  function animate(selector, effect, stagger = 0) {
    document.querySelectorAll(selector).forEach((element, index) => {
      if (targets.has(element)) return;
      targets.add(element);
      element.dataset.effect = effect;
      element.classList.add('motion-ready');
      element.style.setProperty('--motion-delay', `${(index % 3) * stagger}ms`);
      if (effect === 'review') element.style.setProperty('--review-tilt', index % 2 ? '1deg' : '-1deg');
      // Preserve restored scroll positions and content above the current viewport.
      if (element.getBoundingClientRect().bottom < 0) element.classList.add('is-in');
      else observer.observe(element);
    });
  }

  animate('.hero-copy > *, .detail-intro > *', 'rise', 85);
  animate('.principles > span', 'left', 100);
  animate('.services .section-heading > div', 'wipe');
  animate('.services .section-heading > p', 'right');
  animate('.service-card', 'card', 100);
  animate('.service-footer', 'rise');
  animate('.approach-statement', 'left');
  animate('.approach-copy', 'right');
  animate('.process .section-heading, .detail-outcomes .section-heading', 'wipe');
  animate('.steps article', 'step', 140);
  animate('.testimonials .section-heading', 'zoom');
  animate('.questions > div:first-child', 'wipe');
  animate('.faq-list > details', 'row', 75);
  animate('.detail-context > div', 'left');
  animate('.situation-list > li', 'right', 85);
  animate('.prepare > div:first-child', 'left');
  animate('.prepare-copy', 'right');
  animate('.contact > .eyebrow', 'rise');
  animate('.contact > h2', 'zoom');
  animate('.contact > p:not(.eyebrow), .contact > .button, .contact > .contact-note, .contact > .other-service', 'rise', 80);
  animate('footer > *', 'rise', 70);
}
initializeEffects();

// Keyboard navigation must never land on an invisible link or control.
document.addEventListener('focusin', event => {
  let element = event.target;
  while (element && element !== document.body) {
    if (targets.has(element)) {
      element.classList.add('is-in');
      observer?.unobserve(element);
    }
    element = element.parentElement;
  }
});
reducedMotion.addEventListener('change', () => {
  applyMotionChoice();
  queueScroll();
  if (!motionEnabled()) {
    observer?.disconnect();
    targets.forEach(element => element.classList.add('is-in'));
  } else {
    initializeEffects();
  }
});
document.querySelector('.footer-back-top')?.addEventListener('click', event => {
  event.preventDefault();
  header.focus({ preventScroll: true });
  window.scrollTo({ top: 0, behavior: motionEnabled() ? 'smooth' : 'instant' });
});

