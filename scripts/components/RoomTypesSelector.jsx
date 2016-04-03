import React from 'react';

function handleClick(roomType, onChangeType) {
  onChangeType(roomType);
}

class RoomTypesSelector extends React.Component {
  static propTypes = {
    currentType: React.PropTypes.string,
    roomTypes: React.PropTypes.array.isRequired,
    onChangeType: React.PropTypes.func.isRequired,
  };

  constructor(props) {
    super(props);
    this.onChange = this.onChange.bind(this);
  }

  onChange(e) {
    this.props.onChangeType(e.target.value);
  }


  render() {
    const { roomTypes, currentType, onChangeType } = this.props;
    return (
      <div>
        <div className="show-for-small-only">
          {roomTypes ? (
            <select value={currentType} onChange={this.onChange}>
              {roomTypes.map(
                value => <option value={value.type} key={value.type}>{value.name}</option>
              )}
            </select>
            ) : null
          }
        </div>
        <div className="show-for-medium">
          {roomTypes ?
            <ul className="menu vertical">
              {roomTypes.map(
                value =>
                  <li key={value.type}  className={value.type === currentType ? 'active' : ''}>
                    <a onClick={handleClick.bind(this, value.type, onChangeType)}>
                      {value.name}
                      {value.type === currentType ?
                        <i className="fa fa-caret-right pull-right"></i>
                      : null }
                    </a>
                  </li>
              )}
            </ul>
          : null }
        </div>
      </div>
    );
  }
}

export default RoomTypesSelector;
