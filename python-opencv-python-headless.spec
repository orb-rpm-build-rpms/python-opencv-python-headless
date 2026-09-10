# Name-compatibility metapackage.
#
# OpenCV publishes four interchangeable wheels on PyPI that all vendor the same
# cv2 module: opencv-python, opencv-python-headless, and the two -contrib
# variants. Projects pick one by distribution name -- mistral-common[image] and
# vLLM both request opencv-python-headless.
#
# Fedora builds a single package, python3-opencv, from the OpenCV source. It
# provides cv2 (so it is functionally the headless wheel) but advertises only
# the base distribution name python3dist(opencv). Nothing in Fedora claims the
# python3dist(opencv-python-headless) name, so RPM's dependency solver cannot
# satisfy a requirement written against it, even though python3-opencv would
# work at runtime.
#
# This files-less package supplies that missing name and points it at
# python3-opencv. It exists so the PyPI-style requirement resolves for every
# consumer at once, rather than patching opencv-python-headless out of each
# project's generated dependencies (mistral-common, vLLM, ...). The version
# tracks python3-opencv so version constraints (opencv-python-headless >= 4)
# are satisfied; bump it if python3-opencv's major version ever falls behind a
# consumer's floor.

Name:           python-opencv-python-headless
Version:        4.13.0
Release:        %autorelease
Summary:        Dependency name bridge from opencv-python-headless to python3-opencv

License:        MIT
URL:            https://github.com/opencv/opencv-python

BuildArch:      noarch


%description
Compatibility metapackage that maps the PyPI distribution name
opencv-python-headless onto Fedora's python3-opencv. It ships no files; it
only makes requirements written against opencv-python-headless resolvable
using the system OpenCV Python bindings.


%package -n     python3-opencv-python-headless
Summary:        %{summary}
Requires:       python3-opencv >= %{version}
# The names a consumer's dependency generator emits for opencv-python-headless.
Provides:       python3dist(opencv-python-headless) = %{version}
Provides:       python3.14dist(opencv-python-headless) = %{version}

%description -n python3-opencv-python-headless
Compatibility metapackage that maps the PyPI distribution name
opencv-python-headless onto Fedora's python3-opencv. It ships no files; it
only makes requirements written against opencv-python-headless resolvable
using the system OpenCV Python bindings.


%files -n python3-opencv-python-headless
# Intentionally empty: this package only bridges a distribution name.


%changelog
%autochangelog
