import axios from 'axios';

const apiClient = axios.create({
  baseURL: process.env.VUE_APP_API_URL || 'http://127.0.0.1:8000',
  withCredentials: true,
});

export default {
  getGames() {
    return apiClient.get('/api/games/');
  },
  getGame(platformSlug, gameSlug) {
    return apiClient.get(`/api/games/${platformSlug}/${gameSlug}/`);
  },
  createGame(formData) {
    return apiClient.post('/api/games/', formData);
  },
  getPlatforms() {
    return apiClient.get('/api/platforms/');
  },
  getPlatformGames(platformSlug) {
    return apiClient.get(`/api/games/${platformSlug}/`);
  },
  searchGames(query) {
    return apiClient.post('/api/search/', { query });
  },
};
