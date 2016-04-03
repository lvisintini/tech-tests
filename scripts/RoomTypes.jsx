import React from 'react';
import classnames from 'classnames';

import Api from './api';
import RoomTypesSelector from './components/RoomTypesSelector';
import Friends from './components/Friends';

const ICONS = {
  'super-deluxe': <i className="fa fa-star-o"></i>,
  deluxe: <i className="fa fa-thumbs-o-up "></i>,
  shared: <i className="fa fa-users"></i>,
  'animal-friendly': <i className="fa fa-paw"></i>,
};

class RoomTypes extends React.Component {
  static propTypes = {};

  constructor(props) {
    super(props);
    this.api = new Api('/room-types.json', '/friends.json');

    this.state = {
      transition: false,
      zeroHeight: false,
      endTransition: false,
      fullHeight: true,

      friends: [],
      roomTypes: [],
      currentType: null,
    };

    this.api.fetchRoomTypes()
      .then(roomTypes => {
        const currentType = roomTypes[0].type || null;

        this.api.fetchFriends(currentType)
          .then(friends => this.setState({ friends }));

        this.setState({ roomTypes, currentType });
      });

    this.changeRoomType = this.changeRoomType.bind(this);
  }

  changeRoomType(currentType) {
    this.api.fetchFriends(currentType)
      .then(friends => this.setState({ friends }));

    this.setState({
      transition: false,
      zeroHeight: true,
      endTransition: false,
      fullHeight: false,
      currentType,
    });

    setTimeout(() => this.setState({
      transition: true,
      zeroHeight: false,
      tempHeight: true,
      fullHeight: false,
    }), 10);

    setTimeout(() => this.setState({
      transition: false,
      zeroHeight: false,
      tempHeight: false,
      fullHeight: true,
    }), 2000);
  }

  render() {
    const { currentType, roomTypes, friends } = this.state;
    const { transition, zeroHeight, tempHeight, fullHeight } = this.state;
    
    const typeData = roomTypes.find(rt => rt.type === currentType);

    const iconStyle = {
      fontSize: '4em',
      textAlign: 'center',
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
      height: '80px',
    };

    const roomtTypesClases = classnames(
      'room-types-container small-12 medium-9 columns', {
        transition,
        'zero-height': zeroHeight,
        'temp-height': tempHeight,
        'full-height': fullHeight,
      }
    );

    return (
      <div className="row">
        <div className="small-12 columns">
          <h3>Room types</h3>
        </div>
        <div className="small-12 medium-3 columns">
          <RoomTypesSelector currentType={currentType}
                             roomTypes={roomTypes}
                             onChangeType={this.changeRoomType} />
        </div>
          {currentType ?
            <div className={roomtTypesClases}>
              <div className="row">
                <div className="small-3 medium-2 columns" style={iconStyle}>
                  {ICONS[currentType] ?
                    ICONS[currentType] :
                    <i className="fa fa-key"></i>
                  }
                </div>
                <div className="small-9 medium-10 columns">
                  <h2>{`${typeData.name} room`}</h2>
                  <h3>{typeData.short_description}</h3>
                </div>
              </div>
              <hr />
              <div className="row">
                <div className="small-12 columns">
                  <p>{typeData.description}</p>
                </div>
              </div>

              <Friends friends={friends} />

              {typeData.facilities.length > 0 ?
                <div>
                  <div className="row">
                    <div className="small-12 columns">
                      <h4>Facilities</h4>
                    </div>
                  </div>
                  <div className="row small-up-2 medium-up-4">
                    {typeData.facilities.map(
                      (f, i) =>
                        <div key={i}
                             className="column"
                             style={{ paddingTop: "10px", paddingBottom:"510x" }}>
                          <i className="fa fa-check-square-o"></i> {f}
                        </div>
                    )}
                  </div>
                </div>
              : null }
            </div>
          : null }
      </div>
    );
  }
}

export default RoomTypes;
