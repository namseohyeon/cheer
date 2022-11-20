let randomBrightColor = () => {
  let color_r = Math.floor(Math.random() * 127 + 128).toString(16);
  let color_g = Math.floor(Math.random() * 127 + 128).toString(16);
  let color_b = Math.floor(Math.random() * 127 + 128).toString(16);
  return `#${color_r+color_g+color_b}`;
}

for(tag_btn of document.getElementsByClassName('tag_btn')){
  tag_btn.style.backgroundColor = randomBrightColor();
}