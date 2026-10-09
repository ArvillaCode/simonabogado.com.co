// Continuous scrolling with native touch and keyboard navigation.
(() => {
  const viewport = document.querySelector('.review-viewport');
  if (!viewport) return;
  const track = viewport.querySelector('.review-track');
  const group = track.querySelector('.review-group');
  const duplicate = group.cloneNode(true);
  duplicate.setAttribute('aria-hidden', 'true');
  duplicate.setAttribute('inert', '');
  track.append(duplicate);
  let width = 0, position = viewport.scrollLeft, frame = 0, previous = 0;
  let visible = false, hovered = false, focused = false, touching = false, interacting = false;
  let resumeTimer;
  function allowed() {
    return visible && !document.hidden && motionEnabled() && !hovered && !focused && !touching && !interacting && width > 0;
  }
  function sync() {
    duplicate.hidden = !motionEnabled();
    if (!allowed()) {
      cancelAnimationFrame(frame);
      frame = 0;
      previous = 0;
    } else if (!frame) {
      position = viewport.scrollLeft;
      frame = requestAnimationFrame(tick);
    }
  }
  function tick(time) {
    frame = 0;
    if (!allowed()) return;
    if (previous) {
      position = (position + Math.min(time - previous, 50) * .028) % width;
      viewport.scrollLeft = position;
    }
    previous = time;
    frame = requestAnimationFrame(tick);
  }
  function measure() {
    width = group.getBoundingClientRect().width;
    position = viewport.scrollLeft;
    sync();
  }
  function pauseInteraction() {
    interacting = true;
    clearTimeout(resumeTimer);
    sync();
    resumeTimer = setTimeout(() => { interacting = false; sync(); }, 6000);
  }
  viewport.addEventListener('pointerenter', event => {
    if (event.pointerType !== 'mouse') return;
    hovered = true;
    sync();
  });
  viewport.addEventListener('pointerleave', () => { hovered = false; sync(); });
  viewport.addEventListener('focusin', () => { focused = true; sync(); });
  viewport.addEventListener('focusout', () => { focused = false; sync(); });
  viewport.addEventListener('pointerdown', () => { touching = true; sync(); }, { passive: true });
  window.addEventListener('pointerup', () => {
    if (!touching) return;
    touching = false;
    pauseInteraction();
  }, { passive: true });
  window.addEventListener('pointercancel', () => {
    if (!touching) return;
    touching = false;
    pauseInteraction();
  }, { passive: true });
  viewport.addEventListener('wheel', pauseInteraction, { passive: true });
  document.addEventListener('visibilitychange', sync);
  reducedMotion.addEventListener('change', sync);
  if ('ResizeObserver' in window) new ResizeObserver(measure).observe(group);
  else window.addEventListener('resize', measure, { passive: true });
  if ('IntersectionObserver' in window) {
    new IntersectionObserver(entries => {
      visible = entries[0].isIntersecting;
      sync();
    }).observe(viewport);
  } else visible = true;
  measure();
})();
