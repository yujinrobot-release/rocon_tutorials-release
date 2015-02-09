Name:           ros-indigo-gazebo-concert
Version:        0.6.5
Release:        0%{?dist}
Summary:        ROS gazebo_concert package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/gazebo_concert
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-concert-master
Requires:       ros-indigo-concert-msgs
Requires:       ros-indigo-concert-scheduler-requests
Requires:       ros-indigo-concert-service-admin
Requires:       ros-indigo-concert-service-gazebo
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-rocon-app-manager
Requires:       ros-indigo-rocon-apps
Requires:       ros-indigo-rocon-bubble-icons
Requires:       ros-indigo-rocon-python-comms
Requires:       ros-indigo-rocon-python-utils
Requires:       ros-indigo-rocon-uri
Requires:       ros-indigo-rospy
BuildRequires:  ros-indigo-catkin

%description
A simple software concert describing how multiple robots launched in simulation
can be used by the concert framework. This package follows the same pattern as
turtle_concert. It is multi typed gazebo robot version of turtle_concert.
Adopted a lot from segbot_gazebo_concert by Piyush Khandelwal

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Feb 09 2015 Jihoon Lee <jihoonlee.in@gmail.com> - 0.6.5-0
- Autogenerated by Bloom

* Wed Jan 07 2015 Jihoon Lee <jihoonlee.in@gmail.com> - 0.6.4-0
- Autogenerated by Bloom

* Mon Jan 05 2015 Jihoon Lee <jihoonlee.in@gmail.com> - 0.6.3-0
- Autogenerated by Bloom

