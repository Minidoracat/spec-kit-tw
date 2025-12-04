#!/usr/bin/env bash
set -euo pipefail

# get-next-version.sh
# Read version from pyproject.toml and output GitHub Actions variables
# Usage: get-next-version.sh
#
# Note: spec-kit-tw uses pyproject.toml as the single source of truth for version numbers

# Get the latest tag for release notes comparison
LATEST_TAG=$(git describe --tags --abbrev=0 2>/dev/null || echo "v0.0.0")
echo "latest_tag=$LATEST_TAG" >> $GITHUB_OUTPUT
echo "Latest Git tag: $LATEST_TAG"

# Read version from pyproject.toml
VERSION=$(grep '^version = ' pyproject.toml | sed 's/version = "\(.*\)"/\1/')
NEW_VERSION="v$VERSION"

echo "new_version=$NEW_VERSION" >> $GITHUB_OUTPUT
echo "Version from pyproject.toml: $NEW_VERSION"