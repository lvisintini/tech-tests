import React from 'react';

import { WidthProvider, Responsive, GridItem } from 'react-grid-layout'

const Grid = WidthProvider(Responsive);

class PageContainer extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    const layouts = {
      desktop: [
        {i: 'a', x: 0, y: 0, w: 1, h: 1, static: true},
        {i: 'b', x: 1, y: 0, w: 3, h: 1, static: true},
        {i: 'c', x: 4, y: 0, w: 1, h: 1, static: true},
      ],

      mobile: [
        {i: 'a', x: 0, y: 0, w: 1, h: 1, static: true},
        {i: 'b', x: 1, y: 0, w: 3, h: 1, static: true},
        {i: 'c', x: 4, y: 2, w: 1, h: 1, static: true},
      ],
    };
    const cols = {
      desktop: 12,
      mobile: 6,
    };

    const breakpoints = {
      desktop: 1200,
      mobile: 420,
    };

    const style = {
      border: '1px solid black',
    };
    
    return (
      <div style={{width:'80%', margin: '0 auto', backgroundColor: 'red',}}>
        <Grid
            className="layout"
            layouts={layouts}
            autoSize={true}
            breakpoints={breakpoints}
            cols={cols}>

          <div key={'a'} >
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean laoreet faucibus purus, eu luctus ex commodo quis. In sed ligula rutrum, dictum nibh varius, interdum tellus. Nullam urna magna, placerat ac pellentesque at, molestie nec tortor. Maecenas vitae iaculis ex. Curabitur gravida diam tellus, in tempor arcu ullamcorper et. Donec efficitur ante nisl, et porttitor enim lacinia sed. Proin vel nisl nec libero auctor vehicula sed id nibh. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Proin porttitor id massa vel efficitur. Praesent mattis, odio in euismod porta, erat dolor hendrerit neque, ac facilisis arcu lacus et mauris. Integer facilisis, neque nec ultricies tempus, neque purus finibus tortor, nec commodo enim augue ac nisi. Vestibulum vitae justo urna. Sed placerat ornare purus eu lobortis. Donec semper ultrices dignissim. Curabitur sit amet porttitor tellus.

          </div>
          <div key={'b'} style={style}>b</div>
          <div key={'c'} style={style}>c</div>
        </Grid>

        <Grid
            className="layout"
            layouts={layouts}

            breakpoints={breakpoints}
            cols={cols}>

          <div key={'a'} style={style}>a</div>
          <div key={'b'} style={style}>b</div>
          <div key={'c'} style={style}>c</div>
        </Grid>


      </div>
    );
  }
}

export default PageContainer;