import React from 'react';
import { assert } from 'chai';
import Friends from './scripts/components/Friends';

describe('Friends component', () => {

  it('should should provide the right test for no friends', () => {
    const friend = 'Someone';
    const component = new Friends({ friends: friend });
    assert.equal(
      component.renderFriendsText(),
      `${friend} has stayed here`
    );

  });

});