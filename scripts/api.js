import request from 'superagent';

class Api {
  constructor(roomTypesEndpoint, friendEndpoint) {
    this.roomTypesEndpoint = roomTypesEndpoint;
    this.friendEndpoint = friendEndpoint;

    this.fetchRoomTypes = this.fetchRoomTypes.bind(this);
    this.fetchFriends = this.fetchFriends.bind(this);
  }

  fetchRoomTypes() {
    return new Promise((resolve, reject) => {
      request.get(this.roomTypesEndpoint)
        .set('X_REQUESTED_WITH', 'XMLHttpRequest')
        .set('Accept', 'application/json')
        .end((error, response) => {
          if (!error) {
            resolve(response.body.types);
          } else {
            reject(error);
          }
        });
    });
  }

  fetchFriends(roomType) {
    return new Promise((resolve, reject) => {
      request.get(this.friendEndpoint)
        .set('X_REQUESTED_WITH', 'XMLHttpRequest')
        .set('Accept', 'application/json')
        .end((error, response) => {
          if (!error) {
            resolve(response.body[roomType] ? response.body[roomType].friends : []);
          } else {
            reject(error);
          }
        });
    });
  }
}

export default Api;
