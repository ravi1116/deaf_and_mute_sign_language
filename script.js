const video = document.getElementById('video');
const captureBtn = document.getElementById('capture');
const result = document.getElementById('result');

navigator.mediaDevices.getUserMedia({ video: true })
  .then(stream => {
    video.srcObject = stream;
  });

captureBtn.addEventListener('click', () => {
  const canvas = document.createElement('canvas');
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;
  canvas.getContext('2d').drawImage(video, 0, 0);

  const image = canvas.toDataURL('image/jpeg');

  fetch('/analyze_frame', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ image })
  })
  .then(res => res.json())
  .then(data => {
    result.textContent = `Emotion: ${data.emotion} | Response: ${data.chatbot_response}`;
  });
});
