import React from 'react';

class Friends extends React.Component {
  static propTypes = {
    friends: React.PropTypes.array.isRequired,
  };

  constructor(props) {
    super(props);
    this.renderFriendsText = this.renderFriendsText.bind(this);
  }

  renderFriendsText() {
    const friends = this.props.friends.slice();
    friends.sort();
    const firstTwo = friends.slice(0, 2);

    switch (friends.length) {
      case 0:
        return '';
      case 1:
        return `${friends[0]} has stayed here.`;
      case 2:
        return `${firstTwo.join(' and ')} have stayed here.`;
      case 3:
        return `${firstTwo.join(', ')}, and 1 other friend have stayed here.`;
      default:
        return `${firstTwo.join(', ')}, and ${friends.length - 2} other friends have stayed here.`;
    }
  }

  render() {
    if (this.props.friends.length === 0) {
      return null;
    }

    return (
      <div className="row">
        <div className="small-12 columns">
          <p>
            <i className="fa fa-share-alt" style={{ paddingRight: '15px', fontSize: '1.25em' }}></i>
            {this.renderFriendsText()}
          </p>
        </div>
      </div>
    );
  }
}

export default Friends;
