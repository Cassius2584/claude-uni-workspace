// Full Calendar always opens time-grid views scrolled to 06:00. This centres each
// calendar on the red "now" line the first time it appears, then leaves scrolling alone.
const { Plugin } = require("obsidian");

const LINE = ".fc-timegrid-now-indicator-line";

module.exports = class CalendarScrollToNow extends Plugin {
  onload() {
    const done = new WeakSet();

    const centre = (line, tries = 0) => {
      const scroller = line.closest(".fc-scroller");
      if (!scroller || done.has(scroller)) return;
      // Hidden or not laid out yet (e.g. a background tab): try again shortly.
      if (!scroller.clientHeight) {
        if (tries < 20) setTimeout(() => centre(line, tries + 1), 250);
        return;
      }
      done.add(scroller);
      const top =
        line.getBoundingClientRect().top - scroller.getBoundingClientRect().top + scroller.scrollTop;
      scroller.scrollTop = Math.max(0, top - scroller.clientHeight / 2);
    };

    // Wait past Full Calendar's own initial scroll, which would undo ours.
    const later = (line) => setTimeout(() => requestAnimationFrame(() => centre(line)), 300);

    const observer = new MutationObserver((records) => {
      for (const record of records) {
        for (const node of record.addedNodes) {
          if (node.nodeType !== 1) continue;
          if (node.matches(LINE)) later(node);
          else node.querySelectorAll(LINE).forEach(later);
        }
      }
    });
    this.app.workspace.onLayoutReady(() => {
      observer.observe(document.body, { childList: true, subtree: true });
      document.querySelectorAll(LINE).forEach(later);
    });
    this.register(() => observer.disconnect());
  }
};
