import time

from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback

from backend.blockchain.block import Block
from backend.wallet.transaction import Transaction

pnconfig = PNConfiguration()
pnconfig.subscribe_key = 'sub-c-eab091ea-0d0c-11eb-b978-f27038723aa3'
pnconfig.publish_key = 'pub-c-743ef34a-d7b5-430f-9d75-8746cea9aa4e'

CHANNELS = {
    'TEST': 'TEST',
    'BLOCK': 'BLOCK',
    'TRANSACTION': 'TRANSACTION'
}



class Listener(SubscribeCallback):
    def __init__(self, blockchain):
        self.blochchain = blockchain
    def message(self, pubnub, message_object):
        print(f'\n-- Channel: {message_object.cannel} | Message: {message_object.message}')

        if message_object.channel == CHANN['BLOCK']:
            block = message_object.message
            potential_chain = self.blockchain.chain[:]
            potential_chain.append(block)

            try:
                self.blockchian.replace_chain(potential_chain)
            except Exception as e:
                print(f'\n -- did not replace chain: {e}')

class PubSub():
    """
    Handles the publish/subsctibe layer of the application.
    Provides communication between the nodes of the blockchain network.
    """
    def __init__(self, blockchain, transaction_pool):
        self.pubnub = PubNub(pnconfig)
        self.pubnub.subscribe().channels(CHANNELS.values()).execute()
        self.pubnub.add_listener(Listener(blockchain, transaction_pool))

    def publish(self, channel, message):

        self.pubnub.publish().channel(channel).message(message).sync()

    def broadcast_block(self, block):
        self.publish(CHANNELS['BLOCK'], block.to_json())
    
    def broadcast_transaction(self, transaction):
        self.publish(CHANNELS['TRANSACTION'], transaction.to_json())


def main():
    pubsub = PubSub()

    time.sleep(1)

    pubsub.pulish(CHANNELS['TEST'], {'foo' : 'bar'})

if __name__=='__main__':
    main()



















