'''methods file'''

from random import randint


class Methods:

    def makeJson(self, method: str, data: dict) -> dict:
        json = {
            'api_version': '0',
            'auth': self.auth,
            'client': self.client,
            'data': data,
            'method': method
        }
        return json


    async def IsExistUsername(self, username: str) -> dict:
        json = self.makeJson(
            'isExistUsername',
            {
                'username': username.split('@')[-1]
            })
        return self.post(json=json)


    async def GetPostByShareLink(self, share_link: str, profile_id: str = None) -> dict:
        json = self.makeJson(
            'getPostByShareLink',
            {
              'share_string': share_link.split('/')[-1],
              'profile_id': profile_id
            })
        return self.post(json=json)


    async def GetProfileList(self, limit: int = 10, sort: str = 'FromMax', equal: bool = False) -> dict:
        json = self.makeJson(
            'getProfileList',
            {
                'limit': limit,
                'sort': sort,
                'equal': equal
            }
        )
        return self.post(json=json)


    async def GetProfileInfo(self, profile_id: str):
        json = self.makeJson(
            'getMyProfileInfo',
            {
                'profile_id': profile_id
            })
        return self.post(json=json)


    async def Follow(self, followee_id: str, profile_id: str = None) -> dict:
        json = self.makeJson(
            'requestFollow',
            {
              'f_type':'Follow',
              'followee_id': followee_id,
              'profile_id': profile_id
            })
        return self.post(json=json)


    async def UnFollow(self, followee_id: str, profile_id: str = None) -> dict:
        json = self.makeJson(
            'requestFollow',
            {
                'f_type': 'Unfollow',
                'followee_id': followee_id,
                'profile_id': profile_id
            })
        return self.post(json=json)


    async def CreatePage(self, **kwargs) -> dict:
        json = self.makeJson('createPage', {**kwargs})
        return self.post(json=json)


    async def RemovePage(self, profile_id: str, record_id: str) -> dict:
        json = self.makeJson(
            'removeRecord',
            {
             'model': 'Profile',
             'record_id': record_id,
             'profile_id': profile_id
            })
        return self.post(json=json)


    async def UpdateProfile(self, **kwargs) -> dict:
        json = self.makeJson('updateProfile', {**kwargs})
        return self.post(json=json)


    async def AddComment(
            self,
            text: str,
            post_id: str,
            post_profile_id: str,
            profile_id: str = None
    ) -> dict:
        json = self.makeJson(
            'addComment',
            {
              'content': text,
              'post_id': post_id,
              'post_profile_id': post_profile_id,
              'rnd': randint(100000000, 999999999),
              'profile_id': profile_id
            })
        return self.post(json=json)


    async def Like(self, post_id: str, post_profile_id: str, profile_id: str = None) -> dict:
        json = self.makeJson(
            'likePostAction',
            {
              'action_type': 'Like',
              'post_id': post_id,
              'post_profile_id': post_profile_id,
              'profile_id': profile_id
            })
        return self.post(json=json)


    async def UnLike(self, post_id: str, post_profile_id: str, profile_id: str = None) -> dict:
        json = self.makeJson(
            'likePostAction',
            {
              'action_type': 'Unlike',
              'post_id': post_id,
              'post_profile_id': post_profile_id,
              'profile_id': profile_id
            })
        return self.post(json=json)


    async def View(self, post_id: str, post_profile_id: str) -> dict:
        json = self.makeJson(
            'addPostViewCount',
            {
              'post_id': post_id,
              'post_profile_id': post_profile_id
            })
        return self.post(json=json)


    async def GetComments(
            self,
            post_id: str,
            post_profile_id: str,
            profile_id: str = None,
            sort: str = 'FromMax',
            limit: int = 50,
            equal: bool = False
    ) -> dict:
        json = self.makeJson(
            'getComments',
            {
              'equal': equal,
              'limit': limit,
              'sort': sort,
              'post_id': post_id,
              'profile_id': profile_id,
              'post_profile_id': post_profile_id
            })
        return self.post(json=json)

    #
    async def GetProfilePosts(
            self,
            target_profile_id: str,
            profile_id: str = None,
            limit: int = 50,
            sort: str = 'FromMax',
            equal: bool = False
    ) -> dict:
        json = self.makeJson(
            'getRecentFollowingPosts',
            {
              'equal': equal,
              'limit': limit,
              'sort': sort,
              'profile_id': profile_id,
              'target_profile_id': target_profile_id
            })
        return self.post(json=json)


    async def GetProfilesStories(self, profile_id: str, limit: int = 100) -> dict:
        json = self.makeJson(
            'getProfilesStories',
            {
              'limit': limit,
              'profile_id': profile_id
            })
        return self.post(json=json)


    async def GetRecentFollowingPosts(
            self,
            profile_id: str,
            limit: int = 30,
            sort: str = 'FromMax',
            equal: bool = False
    ) -> dict:
        json = self.makeJson(
            'getRecentFollowingPosts',
            {
              'equal': equal,
              'limit': limit,
              'sort': sort,
              'profile_id': profile_id
            })
        return self.post(json=json)




    async def RequestUpLoadFile(
            self,
            profile_id: str,
            file_name: str,
            file_size: int,
            file_type: str
    ) -> dict:
        json = self.makeJson(
            'requestUploadFile',
            {
              'file_name': file_name.split('/')[-1],
              'file_size': file_size,
              'file_type': file_type,
              'profile_id': profile_id
            })
        return self.post(json=json)


    async def GetBookmarkedPosts(
            self,
            profile_id: str,
            limit: int = 50,
            sort: str = 'FromMax',
            equal: bool = False
    ) -> dict:
        json = self.makeJson(
            'getBookmarkedPosts',
            {
              'equal': equal,
              'limit': limit,
              'sort': sort,
              'profile_id': profile_id
              })
        return self.post(json=json)


    async def GetExplorePosts(
            self,
            profile_id: str,
            limit: int = 50,
            sort: str = 'FromMax',
            equal: bool = False,
            max_id: str = None
    ) -> dict:
        json = self.makeJson(
            'getExplorePosts',
            {
              'equal': equal,
              'limit': limit,
              'sort': sort,
              'max_id': max_id,
              'profile_id': profile_id
              })
        return self.post(json=json)


    async def GetBlockedProfiles(
            self,
            profile_id: str,
            limit: int = 50,
            sort: str = 'FromMax',
            equal: bool = False
    ) -> dict:
        json = self.makeJson(
            'getBlockedProfiles',
            {
             'equal': equal,
              'limit': limit,
              'sort': sort,
              'profile_id': profile_id
            })
        return self.post(json=json)


    async def GetProfileFollowers(
            self,
            profile_id: str,
            target_profile_id: str,
            limit: int = 50,
            sort: str = 'FromMax',
            equal: bool = False
    ) -> dict:
        json = self.makeJson(
            'getProfileFollowers',
             {
               'equal': equal,
               'f_type': 'Follower',
               'limit': limit,
               'sort': sort,
               'target_profile_id': target_profile_id,
               'profile_id': profile_id
             })
        return self.post(json=json)


    async def GetProfileFollowings(
            self,
            profile_id: str,
            target_profile_id: str,
            limit: int = 50,
            sort: str = 'FromMax',
            equal: bool = False
    ) -> dict:
        json = self.makeJson(
            'getProfileFollowers',
             {
               'equal': equal,
               'f_type': 'Following',
               'limit': limit,
               'sort': sort,
               'target_profile_id': target_profile_id,
               'profile_id': profile_id
             })
        return self.post(json=json)


    async def BlockProfile(self, profile_id: str, blocked_id: str) -> dict:
        json = self.makeJson(
            'setBlockProfile',
             {
               'action':'Block',
               'blocked_id': blocked_id,
               'profile_id': profile_id
               })
        return self.post(json=json)


    async def UnBlockProfile(self, profile_id: str, blocked_id: str) -> dict:
        json = self.makeJson(
            'setBlockProfile',
             {
               'action': 'Unblock',
               'blocked_id': blocked_id,
               'profile_id': profile_id
               })
        return self.post(json=json)


    async def AddPost(
            self,
            profile_id: str,
            file: str,
            caption: str = None,
            file_type: str = BaseMethod.picture
    ) -> dict:
        result = self.uploadFile(file, profile_id, file_type)
        json = self.makeJson('addPost', {
            'rnd': int(random() * 1e6 + 1),
            'width': 720,
            'height': 720,
            'caption': caption,
            'file_id': result[1]['file_id'],
            'post_type': file_type,
            'profile_id': profile_id,
            'hash_file_receive': result[0]['hash_file_receive'],
            'thumbnail_file_id': result[1]['file_id'],
            'thumbnail_hash_file_receive': result[0]['hash_file_receive'],
            'is_multi_file': False
            })
        return self.post(json=json)
