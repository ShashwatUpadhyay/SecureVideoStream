import React, { use, useEffect, useRef, useState } from 'react';
import Hls from 'hls.js';
import axios from 'axios';

const BASE_URL = 'https://9319j0b7-8000.inc1.devtunnels.ms/'
// const BASE_URL = 'http://127.0.0.1:8000/'


const VideoPlayer = () => {
  const videoRef = useRef(null);
  const [videoUid,setVideoUid] = useState()
  var token = ''
  useEffect(() => {
  const video = videoRef.current;
  const hls = new Hls();
  console.log("Trying fetching  latest-video")
  axios.get(BASE_URL + 'api/latest-video/')
    .then((res) => {
      console.log("Video Fetched: ", res.data.data.uid);
      axios.get(`${BASE_URL}api/generate-token/${res.data.data.uid}/`).then((r) => {
        console.log("Token Generated: ", r.data.token);
        const videoUrl = `${BASE_URL}api/stream-video/${r.data.token}/playlist.m3u8`;
        // const videoUrl = `${BASE_URL}media/hls_videos/${res.data.data.uid}/playlist.m3u8`;
        console.log("setup done: ",videoUrl)

        if (Hls.isSupported()) {
          hls.loadSource(videoUrl);
          hls.attachMedia(video);
          hls.on(Hls.Events.MANIFEST_PARSED, () => {
            video.play().catch(e => console.log('Autoplay blocked:', e));
            document.removeEventListener('click', playVideo);
          });
        } else if (video.canPlayType('application/vnd.apple.mpegurl')) {
          video.src = videoUrl;
          video.addEventListener('loadedmetadata', () => {
            video.play();
          });
        }
      }).catch((e) => {
      console.log('Error while generating token:', e);
    });
    })
    .catch((e) => {
      console.log('Error fetching video UID:', e);
    });

  return () => {
    hls.destroy();
  };
}, []);


  return (
    <div className="w-full max-w-4xl mx-auto p-4 space-y-6">
      <h1 className="text-3xl font-bold text-center">Welcome to the Secure LMS</h1>
      <p className="text-lg text-gray-700 text-center">
        This platform provides secure video lectures for students. All content is protected and streamed via secure technology.
      </p>

      <div className="bg-white p-4 rounded-lg shadow-md">
        <h2 className="text-xl font-semibold mb-2">Today's Lecture</h2>
        <video
          ref={videoRef}
          controls
          className="w-full rounded-xl shadow-lg"
        ></video>
      </div>

      <div className="bg-gray-100 p-4 rounded-lg">
        <h2 className="text-lg font-semibold mb-1">Instructions:</h2>
        <ul className="list-disc list-inside text-gray-700">
          <li>Make sure you have a stable internet connection.</li>
          <li>Do not attempt to record or download the lecture.</li>
          <li>Your activity may be monitored for security purposes.</li>
        </ul>
      </div>
    </div>
  );
};

export default VideoPlayer;