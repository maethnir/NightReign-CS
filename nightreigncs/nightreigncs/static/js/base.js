function openTab(evt, tabName) {
  const characterSection = document.getElementById("character-section")
  // Hide every nightfarer content
  const tabcontent = characterSection.querySelectorAll(".tab-content");
  tabcontent.forEach(tab => tab.style.display = "none");

  // Deactivate every tab
  const tablinks = characterSection.querySelectorAll(".tab-item");
  tablinks.forEach(tab => tab.className = "tab-item");

  // Activate selected nightfarer
  characterSection.querySelector(`#${tabName}`).style.display = "flex";
  // Activate clicked tab
  evt.currentTarget.className += " active";
}

function openLocationTab(evt, tabName) {
  const locationSection = document.getElementById("locations")
  // Hide every column
  const tabcontent = locationSection.querySelectorAll(".locations-column");
  tabcontent.forEach(tab => tab.style.display = "none");

  // Deactivate every tab
  const tablinks = locationSection.querySelectorAll(".tab-item");
  tablinks.forEach(tab => tab.className = "tab-item");

  // Activate selected column
  locationSection.querySelector(`#${tabName}`).style.display = "flex";
  // Activate clicked tab
  evt.currentTarget.className += " active";
}

function toggleEvent(clickedEvent) {
  document.querySelectorAll('.event').forEach(event => {
    const body = event.querySelector('.event-body');
    if (event === clickedEvent) {
      body.classList.toggle('active');
    } else {
      body.classList.remove('active');
    }
  });
}

function openExpeditionModal() {
  const modal = document.getElementById("expedition-modal");
  if (modal) {
    modal.style.display = "flex";
  }
}

function closeExpeditionModal() {
  const modal = document.getElementById("expedition-modal");
  if (modal) {
    modal.style.display = "none";
  }
}

function animateScroll(containerSelector, duration = 15000) {
  const container = document.querySelector(containerSelector);
  if (!container) return;

  const maxScroll = container.scrollHeight - container.clientHeight;
  let direction = 1;
  let start = null;

  function step(timestamp) {
    if (!start) start = timestamp;
    const elapsed = timestamp - start;
    const progress = Math.min(elapsed / duration, 1);

    // Ease-in-out with cosine
    const eased = (1 - Math.cos(progress * Math.PI)) / 2;
    container.scrollTop = direction === 1 ? eased * maxScroll : (1 - eased) * maxScroll;

    if (progress < 1) {
      requestAnimationFrame(step);
    } else {
      direction *= -1;
      start = null;
      requestAnimationFrame(step);
    }
  }

  requestAnimationFrame(step);
}


function selectExpedition(expeditionId) {
  // Toggle displays of each expedition
  const nightlordSection = document.getElementById("nightlord-section");

  const expeditions = nightlordSection.querySelectorAll('.expedition-selection');
  expeditions.forEach(ex => ex.style.display = "none");
  const selectedExpedition = nightlordSection.querySelectorAll(`.expedition-${expeditionId}`);
  selectedExpedition.forEach(ex => ex.style.display = "flex");

  // Close the pop-up
  closeExpeditionModal();
}

window.addEventListener("click", function (event) {
  const modal = document.getElementById("expedition-modal");
  if (event.target === modal) {
    closeExpeditionModal();
  }
});

document.addEventListener("DOMContentLoaded", () => {
  animateScroll("#map-locations");
});
