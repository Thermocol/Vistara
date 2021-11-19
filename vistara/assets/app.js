const inputs = document.querySelectorAll(".input");

function focusFunc() {
  let parent = this.parentNode;
  parent.classList.add("focus");
}

function blurFunc() {
  let parent = this.parentNode;
  if (this.value == "") {
    parent.classList.remove("focus");
  }
}

inputs.forEach((input) => {
  input.addEventListener("focus", focusFunc);
  input.addEventListener("blur", blurFunc);
});

const realFileBtn1 = document.getElementById("real-file1");
const customBtn1 = document.getElementById("custom-button1");
const customTxt1 = document.getElementById("custom-text1");

customBtn1.addEventListener("click", function() {
  realFileBtn1.click();
});

realFileBtn1.addEventListener("change", function() {
  if (realFileBtn1.value) {
    customTxt1.innerHTML = realFileBtn1.value.match(
      /[\/\\]([\w\d\s\.\-\(\)]+)$/
    )[1];
  } else {
    customTxt1.innerHTML = "No file chosen, yet.";
  }
});

const realFileBtn2 = document.getElementById("real-file2");
const customBtn2 = document.getElementById("custom-button2");
const customTxt2 = document.getElementById("custom-text2");

customBtn2.addEventListener("click", function() {
  realFileBtn2.click();
});

realFileBtn2.addEventListener("change", function() {
  if (realFileBtn2.value) {
    customTxt2.innerHTML = realFileBtn2.value.match(
      /[\/\\]([\w\d\s\.\-\(\)]+)$/
    )[1];
  } else {
    customTxt2.innerHTML = "No file chosen, yet.";
  }
});

