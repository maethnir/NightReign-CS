function openTab(evt, tabName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tab-content");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tab-item");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(tabName).style.display = "flex";
  evt.currentTarget.className += " active";
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

window.addEventListener("click", function (event) {
  const modal = document.getElementById("expedition-modal");
  if (event.target === modal) {
    closeExpeditionModal();
  }
});


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

document.addEventListener("DOMContentLoaded", () => {
  const select = document.getElementById("expedition-select");
  if (select && select.value) {
    selectExpedition(select);
  }
});

