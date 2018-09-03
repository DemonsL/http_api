# coding:utf-8
import requests

#产品模块
class Amazon_product():

    def listMatchingProducts(self):
        params = { 'method': 'ListMatchingProducts', 'query': '*','query_context':''}
        return params

    # 根据asin获取商品信息      可以多个 /  最多十个
    def GetMatchingProduct(self):
        asin_list=['B072ZT79V1,B072ZSMQLL,B072ZYKJL7,B072ZZRTTJ']
        params = {'method': 'GetMatchingProduct', 'asin': asin_list}
        return params

    def GetMatchingProductForId(self):
        asin_list = 'B079M1R92S,B079MCGCGQ'
        params = {'method': 'GetMatchingProductForId','id_type':'ASIN','id': asin_list}
        return params

    # 根据sku     获取返回商品的当前有竞争力的价格/排名      sku最多可以传20个
    def GetCompetitivePricingForSKU(self):
        params = {'method': 'GetCompetitivePricingForSKU', 'sku': 'WF-TB1006MJC-Yellow'}
        return params

    # 根据asin    获取返回商品的当前有竞争力的价格/排名      asin最多可以传20个
    def GetCompetitivePricingForASIN(self):
        asin_list = 'B07313N12G,B072ZT79V1'
        params = {'method': 'GetCompetitivePricingForASIN', 'asin': asin_list}
        return params

    #根据 SellerSKU，根据商品状况返回一个指定商品的最低报价    sku最多可以传20个
    def GetLowestOfferListingsForSKU(self):
        sku_list = 'WF-TR16013MJC-Black,WF-TR-MJC001-Black'
        params = {'method': 'GetLowestOfferListingsForSKU', 'sku': sku_list}
        return params

    #根据 ASIN，根据商品状况返回一个指定商品的最低报价    ASIN最多可以传20个
    def GetLowestOfferListingsForASIN(self):
        asin_list = 'B07313N12G,B072ZT79V1'
        params = {'method': 'GetLowestOfferListingsForASIN', 'asin': asin_list}
        return params

    #根据 sku获取商品的价格
    #sku可以传入多个值  最多可以传20个值
    def GetMyPriceForSKU(self):
        sku_list = 'WF-TR16013MJC-Black,WF-TR-MJC001-Black'
        params = {'method': 'GetMyPriceForSKU', 'sku': sku_list}
        return params

    # 根据 asin获取商品的价格
    # ASIN可以传入多个值  最多可以传20个值
    def GetMyPriceForASIN(self):
        asin_list = 'B079M1R92S,B079MCGCGQ'
        params = {'method': 'GetMyPriceForASIN', 'asin': asin_list}
        return params

    #根据sku获取商品的所属类别
    def GetProductCategoriesForSKU(self):
        params = {'method': 'GetProductCategoriesForSKU', 'sku': 'WF-TR-16011MJC-Dark Gray'}
        return params

    # 根据asin获取商品的所属类别
    def GetProductCategoriesForASIN(self):
        params = {'method': 'GetProductCategoriesForASIN', 'asin': 'B079M1R92S'}
        return params

if __name__ == "__main__":
    url = 'http://192.168.55.5:9527/amazon_execute/product'
    default_params = {
        'access_key': 'AKIAJCEFHCKZP4HSI4YQ',
        'mws_token': 'amzn.mws.3eb06cff-080a-e235-8450-54ad35779ddf',
        'seller_id': 'A3PBXV5PH8245N',
        'market_place_id': 'ATVPDKIKX0DER',
        'secret_key': 'sywDqX5kcDhj599L5PD4GA03hHECL8hyS7VIVsbw'
    }

    interface_product = Amazon_product()
    params = interface_product.GetProductCategoriesForSKU()
    default_params.update(params)
    print(default_params)
    res = requests.post(url, default_params)
    print(res.text)

